#include <memory>

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include <DataFormats/PatCandidates/interface/Jet.h>
#include <DataFormats/VertexReco/interface/Vertex.h>
#include <DataFormats/VertexReco/interface/VertexFwd.h>
#include <DataFormats/GsfTrackReco/interface/GsfTrack.h>
#include <DataFormats/GsfTrackReco/interface/GsfTrackFwd.h>
#include <DataFormats/TrackReco/interface/Track.h>
#include <DataFormats/TrackReco/interface/TrackFwd.h>

#include<vector>
#include<TVector3.h>


class PatJetBooster : public edm::EDProducer {
    public:
        explicit PatJetBooster(const edm::ParameterSet&);
        ~PatJetBooster();

    private:
        virtual void beginJob() ;
        virtual void produce(edm::Event&, const edm::EventSetup&);
        virtual void endJob() ;


        edm::InputTag jetTag_;
        edm::InputTag vertexTag_;

};

PatJetBooster::PatJetBooster(const edm::ParameterSet& iConfig) :
    jetTag_(iConfig.getParameter<edm::InputTag>("jetTag")),
    vertexTag_(iConfig.getParameter<edm::InputTag>("vertexTag")) {

    produces<pat::JetCollection>();  
}




void PatJetBooster::produce(edm::Event& iEvent, const edm::EventSetup& iSetup) {

    edm::Handle<edm::View<reco::Candidate> > jetH;
    iEvent.getByLabel(jetTag_,jetH);

    edm::Handle<reco::VertexCollection> vtxH;
    iEvent.getByLabel(vertexTag_,vtxH);

    std::auto_ptr<pat::JetCollection> pOut(new pat::JetCollection);

    reco::Vertex::Point pos(0,0,0);
    if(vtxH->size() > 0) pos = vtxH->at(0).position();

    float mom2, dz, sumDzMom2, sumMom2;
    for(edm::View<reco::Candidate>::const_iterator itJet=jetH->begin(); itJet!=jetH->end(); ++itJet) {    

        pat::Jet clone = *edm::RefToBase<reco::Candidate>(jetH,itJet-jetH->begin()).castTo<pat::JetRef>();

        sumMom2=0; sumDzMom2=0;
        const reco::Track *thisTk;
        for(size_t i=0;i<clone.getPFConstituents().size();++i) {

            if(      clone.getPFConstituent(i)->gsfTrackRef().isNonnull() ) thisTk = &*clone.getPFConstituent(i)->gsfTrackRef();
            else if( clone.getPFConstituent(i)->trackRef().isNonnull()    ) thisTk = &*clone.getPFConstituent(i)->trackRef();
            else continue;

            mom2 = pow(clone.getPFConstituent(i)->pt(),2);
            dz   = thisTk->dz(pos);

            sumDzMom2 += mom2 * dz;
            sumMom2   += mom2;

        }

        if (sumMom2 != 0) {
            clone.addUserFloat("dz",sumDzMom2/sumMom2);
            clone.addUserFloat("mom2",sumMom2);
            clone.addUserFloat("dzMom2",sumDzMom2);
        } else {
            clone.addUserFloat("dz",-9999.9);
            clone.addUserFloat("mom2",-9999.9);
            clone.addUserFloat("dzMom2",-9999.9);
        }

        pOut->push_back(clone);

    }
    iEvent.put(pOut);
}

PatJetBooster::~PatJetBooster() { }
void PatJetBooster::beginJob() { }
void PatJetBooster::endJob() { }
DEFINE_FWK_MODULE(PatJetBooster);