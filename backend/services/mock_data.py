"""Mock data store for testing Legal Assistant API."""
from typing import List, Dict
from models.schemas import LegalChunk, JudgmentChunk, Metadata


# ============================================================================
# Mock Legal Chunks (Acts/Sections)
# ============================================================================

MOCK_LEGAL_CHUNKS: List[Dict] = [
    {
        "id": "BNS_Sec_103",
        "text_for_embedding": "[BNS] > Chapter VI > Section 103 - Murder : Whoever commits murder shall be punished with death or imprisonment for life, and shall also be liable to fine.",
        "raw_content": "103. Murder. Whoever commits murder shall be punished with death or imprisonment for life, and shall also be liable to fine.",
        "metadata": {
            "doc_type": "statute",
            "act_name": "Bharatiya Nyaya Sanhita, 2023",
            "category": "Criminal",
            "chapter": "VI - Of Offences Affecting Life",
            "section_id": "103",
            "chunk_type": "Section",
            "has_illustration": True,
            "has_proviso": False
        }
    },
    {
        "id": "BNS_Sec_104",
        "text_for_embedding": "[BNS] > Chapter VI > Section 104 - Punishment for murder by life-convict : Whoever, being under sentence of imprisonment for life, commits murder, shall be punished with death or with imprisonment for life, which shall mean the remainder of that person's natural life.",
        "raw_content": "104. Punishment for murder by life-convict. Whoever, being under sentence of imprisonment for life, commits murder, shall be punished with death or with imprisonment for life, which shall mean the remainder of that person's natural life.",
        "metadata": {
            "doc_type": "statute",
            "act_name": "Bharatiya Nyaya Sanhita, 2023",
            "category": "Criminal",
            "chapter": "VI - Of Offences Affecting Life",
            "section_id": "104",
            "chunk_type": "Section",
            "has_illustration": False,
            "has_proviso": False
        }
    },
    {
        "id": "BNS_Sec_105",
        "text_for_embedding": "[BNS] > Chapter VI > Section 105 - Culpable homicide not amounting to murder : Culpable homicide is not murder if the offender, whilst deprived of the power of self-control by grave and sudden provocation, causes the death of the person who gave the provocation.",
        "raw_content": "105. Culpable homicide not amounting to murder. Culpable homicide is not murder if the offender, whilst deprived of the power of self-control by grave and sudden provocation, causes the death of the person who gave the provocation or causes the death of any other person by mistake or accident.",
        "metadata": {
            "doc_type": "statute",
            "act_name": "Bharatiya Nyaya Sanhita, 2023",
            "category": "Criminal",
            "chapter": "VI - Of Offences Affecting Life",
            "section_id": "105",
            "chunk_type": "Section",
            "has_illustration": True,
            "has_proviso": True
        }
    },
    {
        "id": "NI_Act_Sec_138",
        "text_for_embedding": "[Negotiable Instruments Act] > Chapter XVII > Section 138 - Dishonour of cheque for insufficiency of funds : Where any cheque drawn by a person on an account maintained by him with a banker for payment of any amount of money to another person from out of that account for the discharge, in whole or in part, of any debt or other liability, is returned by the bank unpaid, either because of the amount of money standing to the credit of that account is insufficient to honour the cheque or that it exceeds the amount arranged to be paid from that account by an agreement made with that bank, such person shall be deemed to have committed an offence.",
        "raw_content": "138. Dishonour of cheque for insufficiency, etc., of funds in the account. Where any cheque drawn by a person on an account maintained by him with a banker for payment of any amount of money to another person from out of that account for the discharge, in whole or in part, of any debt or other liability, is returned by the bank unpaid, either because of the amount of money standing to the credit of that account is insufficient to honour the cheque or that it exceeds the amount arranged to be paid from that account by an agreement made with that bank, such person shall be deemed to have committed an offence and shall, without prejudice to any other provisions of this Act, be punished with imprisonment for a term which may be extended to two years, or with fine which may extend to twice the amount of the cheque, or with both.",
        "metadata": {
            "doc_type": "statute",
            "act_name": "Negotiable Instruments Act, 1881",
            "category": "Commercial",
            "chapter": "XVII - Penalties in Case of Dishonour of Certain Cheques",
            "section_id": "138",
            "chunk_type": "Section",
            "has_illustration": False,
            "has_proviso": True
        }
    },
    {
        "id": "NI_Act_Sec_141",
        "text_for_embedding": "[Negotiable Instruments Act] > Chapter XVII > Section 141 - Offences by companies : If the person committing an offence under section 138 is a company, every person who, at the time the offence was committed, was in charge of, and was responsible to, the company for the conduct of the business of the company, as well as the company, shall be deemed to be guilty of the offence and shall be liable to be proceeded against and punished accordingly.",
        "raw_content": "141. Offences by companies. If the person committing an offence under section 138 is a company, every person who, at the time the offence was committed, was in charge of, and was responsible to, the company for the conduct of the business of the company, as well as the company, shall be deemed to be guilty of the offence and shall be liable to be proceeded against and punished accordingly: Provided that nothing contained in this sub-section shall render any person liable to punishment if he proves that the offence was committed without his knowledge, or that he had exercised all due diligence to prevent the commission of such offence.",
        "metadata": {
            "doc_type": "statute",
            "act_name": "Negotiable Instruments Act, 1881",
            "category": "Commercial",
            "chapter": "XVII - Penalties in Case of Dishonour of Certain Cheques",
            "section_id": "141",
            "chunk_type": "Section",
            "has_illustration": False,
            "has_proviso": True
        }
    },
    {
        "id": "IPC_Sec_302",
        "text_for_embedding": "[IPC] > Chapter XVI > Section 302 - Punishment for murder : Whoever commits murder shall be punished with death, or imprisonment for life, and shall also be liable to fine.",
        "raw_content": "302. Punishment for murder. Whoever commits murder shall be punished with death, or imprisonment for life, and shall also be liable to fine.",
        "metadata": {
            "doc_type": "statute",
            "act_name": "Indian Penal Code, 1860",
            "category": "Criminal",
            "chapter": "XVI - Of Offences Affecting the Human Body",
            "section_id": "302",
            "chunk_type": "Section",
            "has_illustration": False,
            "has_proviso": False
        }
    },
    {
        "id": "IPC_Sec_304",
        "text_for_embedding": "[IPC] > Chapter XVI > Section 304 - Punishment for culpable homicide not amounting to murder : Whoever commits culpable homicide not amounting to murder shall be punished with imprisonment for life, or imprisonment of either description for a term which may extend to ten years, and shall also be liable to fine, if the act by which the death is caused is done with the intention of causing death, or of causing such bodily injury as is likely to cause death.",
        "raw_content": "304. Punishment for culpable homicide not amounting to murder. Whoever commits culpable homicide not amounting to murder shall be punished with imprisonment for life, or imprisonment of either description for a term which may extend to ten years, and shall also be liable to fine, if the act by which the death is caused is done with the intention of causing death, or of causing such bodily injury as is likely to cause death.",
        "metadata": {
            "doc_type": "statute",
            "act_name": "Indian Penal Code, 1860",
            "category": "Criminal",
            "chapter": "XVI - Of Offences Affecting the Human Body",
            "section_id": "304",
            "chunk_type": "Section",
            "has_illustration": False,
            "has_proviso": False
        }
    },
    {
        "id": "BNSS_Sec_482",
        "text_for_embedding": "[BNSS] > Chapter XXXIV > Section 482 - Saving of inherent powers of High Court : Nothing in this Sanhita shall be deemed to limit or affect the inherent powers of the High Court to make such orders as may be necessary to give effect to any order under this Sanhita, or to prevent abuse of the process of any Court or otherwise to secure the ends of justice.",
        "raw_content": "482. Saving of inherent powers of High Court. Nothing in this Sanhita shall be deemed to limit or affect the inherent powers of the High Court to make such orders as may be necessary to give effect to any order under this Sanhita, or to prevent abuse of the process of any Court or otherwise to secure the ends of justice.",
        "metadata": {
            "doc_type": "statute",
            "act_name": "Bharatiya Nagarik Suraksha Sanhita, 2023",
            "category": "Procedural",
            "chapter": "XXXIV - General Provisions",
            "section_id": "482",
            "chunk_type": "Section",
            "has_illustration": False,
            "has_proviso": False
        }
    }
]


# ============================================================================
# Mock Judgment Chunks
# ============================================================================

MOCK_JUDGMENT_CHUNKS: List[Dict] = [
    {
        "id": "judgment_001",
        "text_for_embedding": "Priti Bhojnagarwala vs State Of Gujarat - The court held that the wife, being a deemed director in an association of individuals, is liable under Section 141 of the Negotiable Instruments Act even without signing the cheque. The petition was dismissed.",
        "raw_content": "In this case, the petitioner, wife of the business owner, argued that she should not be held liable under Section 141 of the NI Act as she did not sign the cheque. However, the court held that in an association of individuals, the wife is deemed to be a director and is responsible for the conduct of business. The court observed that vicarious liability extends to all persons in charge of the business at the time of the offence. The petition seeking quashing of proceedings was dismissed.",
        "metadata": {
            "doc_type": "judgment",
            "title": "Priti Bhojnagarwala vs State Of Gujarat",
            "court": "Gujarat High Court",
            "case_type": "Criminal",
            "outcome": "Dismissed",
            "acts_cited": ["NI Act Section 138", "NI Act Section 141"],
            "doc_url": "https://indiankanoon.org/doc/1943657"
        }
    },
    {
        "id": "judgment_002",
        "text_for_embedding": "Rabari Sagarbhai vs State - The court quashed the FIR as the parties had settled the dispute amicably. The court held that continuation of criminal proceedings would amount to abuse of process of law when the dispute is overwhelmingly civil in nature and has been resolved.",
        "raw_content": "The petitioner and the complainant settled the cheque dishonour dispute amicably and filed a joint application for quashing the FIR. The court, exercising powers under Section 482 BNSS, observed that the continuation of criminal proceedings would amount to abuse of process of law and court, and the trial would be futile, as the dispute is overwhelmingly civil in nature and has been resolved. Citing Gian Singh vs State of Punjab, the court allowed the petition and quashed the FIR.",
        "metadata": {
            "doc_type": "judgment",
            "title": "Rabari Sagarbhai vs State",
            "court": "Gujarat High Court",
            "case_type": "Criminal",
            "outcome": "Allowed",
            "acts_cited": ["NI Act Section 138", "BNSS Section 482"],
            "doc_url": "https://indiankanoon.org/doc/example001"
        }
    },
    {
        "id": "judgment_003",
        "text_for_embedding": "State vs Sonu - The court converted the conviction from Section 302 (Murder) to Section 304 (Culpable Homicide) as the accused had inflicted only a solitary blow on the victim's head while the victim was sleeping. The court held that there was no clear intention to kill.",
        "raw_content": "The prosecution argued that the injury on the vital part (head) with brain matter visible indicated murder under Section 302 IPC. However, the defense successfully argued that it was a solitary blow with no repeated attack, and the victim was sleeping, showing no premeditation or clear intent to kill. The court observed that a single blow, though on a vital part, without evidence of intent to cause death, would constitute culpable homicide not amounting to murder. The conviction was converted from Section 302 to Section 304 IPC.",
        "metadata": {
            "doc_type": "judgment",
            "title": "State vs Sonu",
            "court": "Gujarat High Court",
            "case_type": "Criminal",
            "outcome": "Partially Allowed",
            "acts_cited": ["IPC Section 302", "IPC Section 304"],
            "doc_url": "https://indiankanoon.org/doc/example002"
        }
    },
    {
        "id": "judgment_004",
        "text_for_embedding": "Gian Singh vs State of Punjab - Landmark judgment establishing that High Courts can quash criminal proceedings under inherent powers when parties have settled disputes amicably, especially in cases arising out of commercial or civil disputes.",
        "raw_content": "This landmark judgment by the Supreme Court established the principle that High Courts, in exercise of their inherent powers under Section 482 CrPC (now BNSS), can quash criminal proceedings when parties have settled their disputes amicably. The court held that this power should be exercised to prevent abuse of process and secure the ends of justice, particularly in cases where the dispute is essentially civil or commercial in nature.",
        "metadata": {
            "doc_type": "judgment",
            "title": "Gian Singh vs State of Punjab",
            "court": "Supreme Court of India",
            "case_type": "Criminal",
            "outcome": "Allowed",
            "acts_cited": ["CrPC Section 482"],
            "doc_url": "https://indiankanoon.org/doc/example003"
        }
    }
]


# ============================================================================
# Autocomplete Suggestions
# ============================================================================

AUTOCOMPLETE_DATA = [
    "Section 103 - Murder (BNS)",
    "Section 104 - Punishment for murder by life-convict (BNS)",
    "Section 105 - Culpable homicide not amounting to murder (BNS)",
    "Section 138 - Dishonour of cheque (NI Act)",
    "Section 141 - Offences by companies (NI Act)",
    "Section 302 - Punishment for murder (IPC)",
    "Section 304 - Culpable homicide not amounting to murder (IPC)",
    "Section 482 - Inherent powers of High Court (BNSS)",
    "Bharatiya Nyaya Sanhita, 2023",
    "Negotiable Instruments Act, 1881",
    "Indian Penal Code, 1860",
    "Bharatiya Nagarik Suraksha Sanhita, 2023"
]


# ============================================================================
# Helper Functions
# ============================================================================

def get_all_legal_chunks() -> List[LegalChunk]:
    """Get all legal chunks as Pydantic models."""
    return [LegalChunk(**chunk) for chunk in MOCK_LEGAL_CHUNKS]


def get_all_judgment_chunks() -> List[JudgmentChunk]:
    """Get all judgment chunks as Pydantic models."""
    return [JudgmentChunk(**chunk) for chunk in MOCK_JUDGMENT_CHUNKS]


def get_all_chunks() -> List[LegalChunk | JudgmentChunk]:
    """Get all chunks (legal + judgments)."""
    return get_all_legal_chunks() + get_all_judgment_chunks()
