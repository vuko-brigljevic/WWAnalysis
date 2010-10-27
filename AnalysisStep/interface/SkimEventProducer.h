#ifndef MYPRODUCERS_SKIMEVENTPRODUCER_SKIMEVENTPRODUCER_H
#define MYPRODUCERS_SKIMEVENTPRODUCER_SKIMEVENTPRODUCER_H

#include <memory>

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "WWAnalysis/DataFormats/interface/SkimEvent.h"

class SkimEventProducer : public edm::EDProducer {
    public:
        explicit SkimEventProducer(const edm::ParameterSet&);
        ~SkimEventProducer();

    private:
        virtual void beginJob() ;
        virtual void produce(edm::Event&, const edm::EventSetup&);
        virtual void endJob() ;

        std::string branchAlias_;
	reco::SkimEvent::hypoType hypoType_;
        edm::InputTag muTag_;
        edm::InputTag elTag_;
        edm::InputTag extraMuTag_;
        edm::InputTag extraElTag_;
        edm::InputTag jetTag_;
        edm::InputTag pfMetTag_;
        edm::InputTag tcMetTag_;
        edm::InputTag vtxTag_;

};

#endif
