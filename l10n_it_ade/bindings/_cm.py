# flake8: noqa
# -*- coding: utf-8 -*-
# ./_cm.py
# PyXB bindings for NM:6d05a298a781c71d177aab761a79c5e637d7f467
# Generated 2017-10-03 10:08:19.849710 by PyXB version 1.2.4 using Python 2.7.5.final.0
# by Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>
# Namespace urn:www.agenziaentrate.gov.it:specificheTecniche:common [xmlns:cm]
from __future__ import unicode_literals

import io
import logging

_logger = logging.getLogger(__name__)
try:
    import pyxb
    import pyxb.binding
    import pyxb.binding.saxer
    import pyxb.utils.utility
    import pyxb.utils.domutils
    import pyxb.utils.six as _six
except ImportError as err:
    _logger.debug(err)

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier(
    'urn:uuid:faf43498-a811-11e7-95f5-005056ba06a2')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.4'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
try:
    import pyxb.binding.datatypes
except ImportError as err:
    _logger.debug(err)

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(
    'urn:www.agenziaentrate.gov.it:specificheTecniche:common', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])


def CreateFromDocument(xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(
        fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance


def CreateFromDOM(node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type:
# {urn:www.agenziaentrate.gov.it:specificheTecniche:common}Identificativo_Type
class IdentificativoType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(
        Namespace, 'Identificativo_Type')
    _XSDLocation = pyxb.utils.utility.Location(
        '../data/common/fornitura_v3.xsd', 27, 1)
    _Documentation = None


IdentificativoType._CF_pattern = pyxb.binding.facets.CF_pattern()
IdentificativoType._CF_pattern.addPattern(
    pattern='[0-9]{4}[1-9]|[0-9]{3}[1-9][0-9]|[0-9]{2}[1-9][0-9]{2}|[0-9][1-9][0-9]{3}|[1-9][0-9]{4}')
IdentificativoType._InitializeFacetMap(Identificativo_Type._CF_pattern)
Namespace.addCategoryObject(
    'typeBinding', 'Identificativo_Type', IdentificativoType)

# Atomic simple type:
# {urn:www.agenziaentrate.gov.it:specificheTecniche:common}DatoAN_Type


class DatoANType (pyxb.binding.datatypes.string):

    """Tipo semplice costituito da caratteri alfanumerici maiuscoli e dai caratteri: punto, virgola, apice, trattino, spazio, barra semplice, °, ^, ampersand, parentesi aperta e chiusa, doppie virgolette, barra rovesciata, la barra dritta, il più, le maiuscole accentate e la Ü. Tali caratteri non sono ammesi come primo carattere tranne: i numeri da 0 a 9, i caratteri maiuscoli da A a Z, il meno e le dopppie virgolette."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DatoAN_Type')
    _XSDLocation = pyxb.utils.utility.Location(
        '../data/common/typesDati_v3.xsd', 15, 1)
    _Documentation = 'Tipo semplice costituito da caratteri alfanumerici maiuscoli e dai caratteri: punto, virgola, apice, trattino, spazio, barra semplice, \xb0, ^, ampersand, parentesi aperta e chiusa, doppie virgolette, barra rovesciata, la barra dritta, il pi\xf9, le maiuscole accentate e la \xdc. Tali caratteri non sono ammesi come primo carattere tranne: i numeri da 0 a 9, i caratteri maiuscoli da A a Z, il meno e le dopppie virgolette.'


DatoANType._CF_pattern = pyxb.binding.facets.CF_pattern()
DatoANType._CF_pattern.addPattern(
    pattern='([0-9A-Z\\-]|"){1}([ 0-9A-Z&]|\'|\\-|\\.|,|/|\xb0|\\^|\\(|\\)|\xc0|\xc8|\xc9|\xcc|\xd2|\xd9|\xdc|"|\\\\|\\||\\+)*')
DatoANType._InitializeFacetMap(DatoAN_Type._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'DatoAN_Type', DatoANType)

# Atomic simple type:
# {urn:www.agenziaentrate.gov.it:specificheTecniche:common}DatoNU_Type


class DatoNUType (pyxb.binding.datatypes.string):

    """Tipo semplice che identifica numeri naturali positivi e negativi con al massimo 16 cifre."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DatoNU_Type')
    _XSDLocation = pyxb.utils.utility.Location(
        '../data/common/typesDati_v3.xsd', 23, 1)
    _Documentation = 'Tipo semplice che identifica numeri naturali positivi e negativi con al massimo 16 cifre.'


DatoNUType._CF_maxLength = pyxb.binding.facets.CF_maxLength(
    value=pyxb.binding.datatypes.nonNegativeInteger(16))
DatoNUType._CF_pattern = pyxb.binding.facets.CF_pattern()
DatoNUType._CF_pattern.addPattern(pattern='(\\-[1-9]|[1-9])[0-9]*')
DatoNUType._InitializeFacetMap(DatoNU_Type._CF_maxLength,
                                DatoNUType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'DatoNU_Type', DatoNUType)

# Atomic simple type:
# {urn:www.agenziaentrate.gov.it:specificheTecniche:common}DatoPC_Type


class DatoPCType (pyxb.binding.datatypes.string):

    """Tipo semplice che esprime una percentuale e dunque consente valori positivi non superiori a 100, con al massimo 2 cifre decimali. Il separatore decimale previsto è la virgola."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DatoPC_Type')
    _XSDLocation = pyxb.utils.utility.Location(
        '../data/common/typesDati_v3.xsd', 32, 1)
    _Documentation = 'Tipo semplice che esprime una percentuale e dunque consente valori positivi non superiori a 100, con al massimo 2 cifre decimali. Il separatore decimale previsto \xe8 la virgola.'


DatoPCType._CF_maxLength = pyxb.binding.facets.CF_maxLength(
    value=pyxb.binding.datatypes.nonNegativeInteger(16))
DatoPCType._CF_pattern = pyxb.binding.facets.CF_pattern()
DatoPCType._CF_pattern.addPattern(
    pattern='[0-9]?[0-9](,\\d{1,3})?|100(,0{1,3})?')
DatoPCType._InitializeFacetMap(DatoPC_Type._CF_maxLength,
                                DatoPCType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'DatoPC_Type', DatoPCType)

# Atomic simple type:
# {urn:www.agenziaentrate.gov.it:specificheTecniche:common}DatoQU_Type


class DatoQUType (pyxb.binding.datatypes.string):

    """Tipo semplice che identifica numeri positivi con al massimo 5 cifre decimali. La lunghezza massima prevista è di 16 caratteri, il separatore decimale previsto è la virgola."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DatoQU_Type')
    _XSDLocation = pyxb.utils.utility.Location(
        '../data/common/typesDati_v3.xsd', 41, 1)
    _Documentation = 'Tipo semplice che identifica numeri positivi con al massimo 5 cifre decimali. La lunghezza massima prevista \xe8 di 16 caratteri, il separatore decimale previsto \xe8 la virgola.'


DatoQUType._CF_maxLength = pyxb.binding.facets.CF_maxLength(
    value=pyxb.binding.datatypes.nonNegativeInteger(16))
DatoQUType._CF_pattern = pyxb.binding.facets.CF_pattern()
DatoQUType._CF_pattern.addPattern(pattern='[0-9]+(,[0-9]{1,5})?')
DatoQUType._InitializeFacetMap(DatoQU_Type._CF_maxLength,
                                DatoQUType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'DatoQU_Type', DatoQUType)

# Atomic simple type:
# {urn:www.agenziaentrate.gov.it:specificheTecniche:common}DatoVP_Type


class DatoVPType (pyxb.binding.datatypes.string):

    """Tipo semplice che identifica numeri positivi con 2 cifre decimali. La lunghezza massima prevista è di 16 caratteri, il separatore decimale previsto è la virgola."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DatoVP_Type')
    _XSDLocation = pyxb.utils.utility.Location(
        '../data/common/typesDati_v3.xsd', 50, 1)
    _Documentation = 'Tipo semplice che identifica numeri positivi con 2 cifre decimali. La lunghezza massima prevista \xe8 di 16 caratteri, il separatore decimale previsto \xe8 la virgola.'


DatoVPType._CF_maxLength = pyxb.binding.facets.CF_maxLength(
    value=pyxb.binding.datatypes.nonNegativeInteger(16))
DatoVPType._CF_pattern = pyxb.binding.facets.CF_pattern()
DatoVPType._CF_pattern.addPattern(pattern='[0-9]+,[0-9]{2}')
DatoVPType._InitializeFacetMap(DatoVP_Type._CF_maxLength,
                                DatoVPType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'DatoVP_Type', DatoVPType)

# Atomic simple type:
# {urn:www.agenziaentrate.gov.it:specificheTecniche:common}DatoN1_Type


class DatoN1Type (pyxb.binding.datatypes.string):

    """Tipo semplice che identifica i numeri naturali da 1 a 9."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DatoN1_Type')
    _XSDLocation = pyxb.utils.utility.Location(
        '../data/common/typesDati_v3.xsd', 59, 1)
    _Documentation = 'Tipo semplice che identifica i numeri naturali da 1 a 9.'


DatoN1Type._CF_maxLength = pyxb.binding.facets.CF_maxLength(
    value=pyxb.binding.datatypes.nonNegativeInteger(1))
DatoN1Type._CF_pattern = pyxb.binding.facets.CF_pattern()
DatoN1Type._CF_pattern.addPattern(pattern='[1-9]')
DatoN1Type._InitializeFacetMap(DatoN1_Type._CF_maxLength,
                                DatoN1Type._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'DatoN1_Type', DatoN1Type)

# Atomic simple type:
# {urn:www.agenziaentrate.gov.it:specificheTecniche:common}DatoNP_Type


class DatoNPType (pyxb.binding.datatypes.string):

    """Tipo semplice che identifica numeri naturali positivi con al massimo 16 cifre."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DatoNP_Type')
    _XSDLocation = pyxb.utils.utility.Location(
        '../data/common/typesDati_v3.xsd', 68, 1)
    _Documentation = 'Tipo semplice che identifica numeri naturali positivi con al massimo 16 cifre.'


DatoNPType._CF_pattern = pyxb.binding.facets.CF_pattern()
DatoNPType._CF_pattern.addPattern(pattern='[1-9]{1}[0-9]*')
DatoNPType._InitializeFacetMap(DatoNP_Type._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'DatoNP_Type', DatoNPType)

# Atomic simple type:
# {urn:www.agenziaentrate.gov.it:specificheTecniche:common}DatoPI_Type


class DatoPIType (pyxb.binding.datatypes.string):

    """Tipo semplice che identifica la partita IVA rispettandone i vincoli di struttura. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DatoPI_Type')
    _XSDLocation = pyxb.utils.utility.Location(
        '../data/common/typesDati_v3.xsd', 76, 1)
    _Documentation = 'Tipo semplice che identifica la partita IVA rispettandone i vincoli di struttura. '


DatoPIType._CF_length = pyxb.binding.facets.CF_length(
    value=pyxb.binding.datatypes.nonNegativeInteger(11))
DatoPIType._CF_pattern = pyxb.binding.facets.CF_pattern()
DatoPIType._CF_pattern.addPattern(pattern='[0-7][0-9]{10}')
DatoPIType._InitializeFacetMap(DatoPI_Type._CF_length,
                                DatoPIType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'DatoPI_Type', DatoPIType)

# Atomic simple type:
# {urn:www.agenziaentrate.gov.it:specificheTecniche:common}DatoCN_Type


class DatoCNType (pyxb.binding.datatypes.string):

    """Tipo semplice che identifica un codice fiscale numerico rispettandone i vincoli di struttura."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DatoCN_Type')
    _XSDLocation = pyxb.utils.utility.Location(
        '../data/common/typesDati_v3.xsd', 85, 1)
    _Documentation = 'Tipo semplice che identifica un codice fiscale numerico rispettandone i vincoli di struttura.'


DatoCNType._CF_length = pyxb.binding.facets.CF_length(
    value=pyxb.binding.datatypes.nonNegativeInteger(11))
DatoCNType._CF_pattern = pyxb.binding.facets.CF_pattern()
DatoCNType._CF_pattern.addPattern(pattern='[0-9]{11}')
DatoCNType._InitializeFacetMap(DatoCN_Type._CF_length,
                                DatoCNType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'DatoCN_Type', DatoCNType)

# Atomic simple type:
# {urn:www.agenziaentrate.gov.it:specificheTecniche:common}DatoCF_Type


class DatoCFType (pyxb.binding.datatypes.string):

    """Tipo semplice che identifica un codice fiscale provvisorio o alfanumerico rispettandone i vincoli di struttura."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DatoCF_Type')
    _XSDLocation = pyxb.utils.utility.Location(
        '../data/common/typesDati_v3.xsd', 94, 1)
    _Documentation = 'Tipo semplice che identifica un codice fiscale provvisorio o alfanumerico rispettandone i vincoli di struttura.'


DatoCFType._CF_pattern = pyxb.binding.facets.CF_pattern()
DatoCFType._CF_pattern.addPattern(
    pattern='[0-9]{11}|[A-Z]{6}[0-9LMNPQRSTUV]{2}[A-Z]{1}[0-9LMNPQRSTUV]{2}[A-Z]{1}[0-9LMNPQRSTUV]{3}[A-Z]{1}')
DatoCFType._InitializeFacetMap(DatoCF_Type._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'DatoCF_Type', DatoCFType)

# Atomic simple type:
# {urn:www.agenziaentrate.gov.it:specificheTecniche:common}DatoCB_Type


class DatoCBType (pyxb.binding.datatypes.byte):

    """Tipo semplice che consente esclusivamente i valori 0 e 1."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DatoCB_Type')
    _XSDLocation = pyxb.utils.utility.Location(
        '../data/common/typesDati_v3.xsd', 102, 1)
    _Documentation = 'Tipo semplice che consente esclusivamente i valori 0 e 1.'


DatoCBType._CF_pattern = pyxb.binding.facets.CF_pattern()
DatoCBType._CF_pattern.addPattern(pattern='[01]')
DatoCBType._InitializeFacetMap(DatoCB_Type._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'DatoCB_Type', DatoCBType)

# Atomic simple type:
# {urn:www.agenziaentrate.gov.it:specificheTecniche:common}DatoCB12_Type


class DatoCB12Type (pyxb.binding.datatypes.byte):

    """Tipo semplice che consente esclusivamente 12 caratteri con i valori 0 e 1."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DatoCB12_Type')
    _XSDLocation = pyxb.utils.utility.Location(
        '../data/common/typesDati_v3.xsd', 110, 1)
    _Documentation = 'Tipo semplice che consente esclusivamente 12 caratteri con i valori 0 e 1.'


DatoCB12Type._CF_pattern = pyxb.binding.facets.CF_pattern()
DatoCB12Type._CF_pattern.addPattern(pattern='[10]{12}')
DatoCB12Type._InitializeFacetMap(DatoCB12_Type._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'DatoCB12_Type', DatoCB12Type)

# Atomic simple type:
# {urn:www.agenziaentrate.gov.it:specificheTecniche:common}DatoDT_Type


class DatoDTType (pyxb.binding.datatypes.string):

    """Tipo semplice che identifica una data nel formato ggmmaaaa. La data indicata non deve essere successiva alla data corrente."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DatoDT_Type')
    _XSDLocation = pyxb.utils.utility.Location(
        '../data/common/typesDati_v3.xsd', 118, 1)
    _Documentation = 'Tipo semplice che identifica una data nel formato ggmmaaaa. La data indicata non deve essere successiva alla data corrente.'


DatoDTType._CF_length = pyxb.binding.facets.CF_length(
    value=pyxb.binding.datatypes.nonNegativeInteger(8))
DatoDTType._CF_pattern = pyxb.binding.facets.CF_pattern()
DatoDTType._CF_pattern.addPattern(
    pattern='(((0[1-9]|[12][0-9]|3[01])(0[13578]|10|12)(\\d{4}))|(([0][1-9]|[12][0-9]|30)(0[469]|11)(\\d{4}))|((0[1-9]|1[0-9]|2[0-8])(02)(\\d{4}))|((29)(02)([02468][048]00))|((29)(02)([13579][26]00))|((29)(02)([0-9][0-9][0][48]))|((29)(02)([0-9][0-9][2468][048]))|((29)(02)([0-9][0-9][13579][26])))')
DatoDTType._InitializeFacetMap(DatoDT_Type._CF_length,
                                DatoDTType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'DatoDT_Type', DatoDTType)

# Atomic simple type:
# {urn:www.agenziaentrate.gov.it:specificheTecniche:common}DatoDA_Type


class DatoDAType (pyxb.binding.datatypes.string):

    """Tipo semplice che identifica un anno nel formato aaaa. Sono ammessi anni dal 1800 al 2099."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DatoDA_Type')
    _XSDLocation = pyxb.utils.utility.Location(
        '../data/common/typesDati_v3.xsd', 127, 1)
    _Documentation = 'Tipo semplice che identifica un anno nel formato aaaa. Sono ammessi anni dal 1800 al 2099.'


DatoDAType._CF_length = pyxb.binding.facets.CF_length(
    value=pyxb.binding.datatypes.nonNegativeInteger(4))
DatoDAType._CF_pattern = pyxb.binding.facets.CF_pattern()
DatoDAType._CF_pattern.addPattern(pattern='(18|19|20)[0-9]{2}')
DatoDAType._InitializeFacetMap(DatoDA_Type._CF_length,
                                DatoDAType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'DatoDA_Type', DatoDAType)

# Atomic simple type:
# {urn:www.agenziaentrate.gov.it:specificheTecniche:common}DatoDN_Type


class DatoDNType (pyxb.binding.datatypes.string):

    """Tipo semplice che identifica una data nel formato ggmmaaaa."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DatoDN_Type')
    _XSDLocation = pyxb.utils.utility.Location(
        '../data/common/typesDati_v3.xsd', 136, 1)
    _Documentation = 'Tipo semplice che identifica una data nel formato ggmmaaaa.'


DatoDNType._CF_length = pyxb.binding.facets.CF_length(
    value=pyxb.binding.datatypes.nonNegativeInteger(8))
DatoDNType._CF_pattern = pyxb.binding.facets.CF_pattern()
DatoDNType._CF_pattern.addPattern(
    pattern='(((0[1-9]|[12][0-9]|3[01])(0[13578]|10|12)(\\d{4}))|(([0][1-9]|[12][0-9]|30)(0[469]|11)(\\d{4}))|((0[1-9]|1[0-9]|2[0-8])(02)(\\d{4}))|((29)(02)([02468][048]00))|((29)(02)([13579][26]00))|((29)(02)([0-9][0-9][0][48]))|((29)(02)([0-9][0-9][2468][048]))|((29)(02)([0-9][0-9][13579][26])))')
DatoDNType._InitializeFacetMap(DatoDN_Type._CF_length,
                                DatoDNType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'DatoDN_Type', DatoDNType)

# Atomic simple type:
# {urn:www.agenziaentrate.gov.it:specificheTecniche:common}DatoD6_Type


class DatoD6Type (pyxb.binding.datatypes.string):

    """Tipo semplice che identifica una data nel formato mmaaaa."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DatoD6_Type')
    _XSDLocation = pyxb.utils.utility.Location(
        '../data/common/typesDati_v3.xsd', 145, 1)
    _Documentation = 'Tipo semplice che identifica una data nel formato mmaaaa.'


DatoD6Type._CF_length = pyxb.binding.facets.CF_length(
    value=pyxb.binding.datatypes.nonNegativeInteger(6))
DatoD6Type._CF_pattern = pyxb.binding.facets.CF_pattern()
DatoD6Type._CF_pattern.addPattern(
    pattern='((0[0-9])|(1[0-2]))((19|20)[0-9][0-9])')
DatoD6Type._InitializeFacetMap(DatoD6_Type._CF_length,
                                DatoD6Type._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'DatoD6_Type', DatoD6Type)

# Atomic simple type:
# {urn:www.agenziaentrate.gov.it:specificheTecniche:common}DatoEM_Type


class DatoEMType (pyxb.binding.datatypes.string):

    """Tipo semplice che identifica un elemento di tipo email"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DatoEM_Type')
    _XSDLocation = pyxb.utils.utility.Location(
        '../data/common/typesDati_v3.xsd', 154, 1)
    _Documentation = 'Tipo semplice che identifica un elemento di tipo email'


DatoEMType._CF_pattern = pyxb.binding.facets.CF_pattern()
DatoEMType._CF_pattern.addPattern(
    pattern='[a-zA-Z0-9._%\\-\'"?^~=]+@[a-zA-Z0-9.\\-]+\\.[a-zA-Z]{2,4}')
DatoEMType._InitializeFacetMap(DatoEM_Type._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'DatoEM_Type', DatoEMType)

# Atomic simple type:
# {urn:www.agenziaentrate.gov.it:specificheTecniche:common}DatoGA_Type


class DatoGAType (pyxb.binding.datatypes.string):

    """Tipo semplice che identifica il numero di giorni in un anno e va da 1 a 365"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DatoGA_Type')
    _XSDLocation = pyxb.utils.utility.Location(
        '../data/common/typesDati_v3.xsd', 162, 1)
    _Documentation = 'Tipo semplice che identifica il numero di giorni in un anno e va da 1 a 365'


DatoGAType._CF_maxLength = pyxb.binding.facets.CF_maxLength(
    value=pyxb.binding.datatypes.nonNegativeInteger(3))
DatoGAType._CF_pattern = pyxb.binding.facets.CF_pattern()
DatoGAType._CF_pattern.addPattern(
    pattern='[1-9]|([1-9][0-9])|([12][0-9][0-9])|(3[0-5][0-9])|(36[0-5])')
DatoGAType._CF_minLength = pyxb.binding.facets.CF_minLength(
    value=pyxb.binding.datatypes.nonNegativeInteger(1))
DatoGAType._InitializeFacetMap(DatoGA_Type._CF_maxLength,
                                DatoGAType._CF_pattern,
                                DatoGAType._CF_minLength)
Namespace.addCategoryObject('typeBinding', 'DatoGA_Type', DatoGAType)

# Atomic simple type:
# {urn:www.agenziaentrate.gov.it:specificheTecniche:common}DatoTL_Type


class DatoTLType (pyxb.binding.datatypes.string):

    """Tipo semplice che identifica un elemento di tipo telefono"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DatoTL_Type')
    _XSDLocation = pyxb.utils.utility.Location(
        '../data/common/typesDati_v3.xsd', 172, 1)
    _Documentation = 'Tipo semplice che identifica un elemento di tipo telefono'


DatoTLType._CF_pattern = pyxb.binding.facets.CF_pattern()
DatoTLType._CF_pattern.addPattern(pattern='[0-9]*')
DatoTLType._InitializeFacetMap(DatoTL_Type._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'DatoTL_Type', DatoTLType)

# Atomic simple type:
# {urn:www.agenziaentrate.gov.it:specificheTecniche:common}DatoCP_Type


class DatoCPType (pyxb.binding.datatypes.string):

    """Tipo semplice che identifica un elemento di tipo cap"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DatoCP_Type')
    _XSDLocation = pyxb.utils.utility.Location(
        '../data/common/typesDati_v3.xsd', 180, 1)
    _Documentation = 'Tipo semplice che identifica un elemento di tipo cap'


DatoCPType._CF_pattern = pyxb.binding.facets.CF_pattern()
DatoCPType._CF_pattern.addPattern(pattern='[0-9]{5}')
DatoCPType._InitializeFacetMap(DatoCP_Type._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'DatoCP_Type', DatoCPType)

# Atomic simple type:
# {urn:www.agenziaentrate.gov.it:specificheTecniche:common}ProvincieItaliane


class ProvincieItaliane (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
                        Elenco delle provincie italiane in vigore, valori ammessi:

                                Agrigento				AG
                                Alessandria				AL
                                Ancona					AN
                                Aosta   				AO
                                Ascoli Piceno			AP
                                L'Aquila				AQ
                                Arezzo					AR
                                Asti					AT
                                Avellino				AV
                                Bari					BA
                                Bergamo					BG
                                Biella					BI
                                Belluno					BL
                                Benevento				BN
                                Bologna					BO
                                Brindisi				BR
                                Brescia					BS
                                Barletta-Andria-Trani	BT
                                Bolzano					BZ
                                Cagliari				CA
                                Campobasso				CB
                                Caserta					CE
                                Chieti					CH
                                Carbonia-Iglessias		CI
                                Caltanissetta			CL
                                Cuneo					CN
                                Como					CO
                                Cremona					CR
                                Cosenza					CS
                                Catania					CT
                                Catanzaro				CZ
                                Enna					EN
                                Forlì-Cesena			FC
                                Ferrara					FE
                                Foggia					FG
                                Firenze					FI
                                Fermo					FM
                                Frosinone				FR
                                Genova					GE
                                Gorizia					GO
                                Grosseto				GR
                                Imperia					IM
                                Isernia					IS
                                Crotone					KR
                                Lecco					LC
                                Lecce					LE
                                Livorno					LI
                                Lodi					LO
                                Latina					LT
                                Lucca					LU
                                Monza e Brianza			MB
                                Macerata				MC
                                Messina					ME
                                Milano					MI
                                Mantova					MN
                                Modena					MO
                                Massa e Carrara			MS
                                Matera					MT
                                Napoli					NA
                                Novara					NO
                                Nuoro					NU
                                Ogliastra				OG
                                Oristano				OR
                                Olbia-Tempio			OT
                                Palermo					PA
                                Piacenza				PC
                                Padova					PD
                                Pescara					PE
                                Perugia					PG
                                Pisa					PI
                                Pordenone				PN
                                Prato					PO
                                Parma					PR
                                Pistoia					PT
                                Pesaro e Urbino			PU
                                Pavia					PV
                                Potenza					PZ
                                Ravenna					RA
                                Reggio Calabria			RC
                                Reggio Emilia			RE
                                Ragusa					RG
                                Rieti					RI
                                Roma					RM
                                Rimini					RN
                                Rovigo					RO
                                Salerno					SA
                                iena					SI
                                Sondrio					SO
                                La Spezia				SP
                                Siracusa				SR
                                Sassari					SS
                                Savona					SV
                                Taranto					TA
                                Teramo					TE
                                Trento 					TN
                                Torino					TO
                                Trapani					TP
                                Terni					TR
                                Trieste					TS
                                Treviso					TV
                                Udine					UD
                                Varese					VA
                                Verbano-Cusio-Ossola	VB
                                Vercelli				VC
                                Venezia					VE
                                Vicenza					VI
                                Verona					VR
                                Medio Campidano			VS
                                Viterbo					VT
                                Vibo Valentia			VV

                        """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ProvincieItaliane')
    _XSDLocation = pyxb.utils.utility.Location(
        '../data/common/typesProvincie_v3.xsd', 30, 1)
    _Documentation = "\n\t\t\tElenco delle provincie italiane in vigore, valori ammessi:\n\t\t\t\n\t\t\t\tAgrigento\t\t\t\tAG\n\t\t\t\tAlessandria\t\t\t\tAL\n\t\t\t\tAncona\t\t\t\t\tAN\n\t\t\t\tAosta   \t\t\t\tAO\n\t\t\t\tAscoli Piceno\t\t\tAP\n\t\t\t\tL'Aquila\t\t\t\tAQ\n\t\t\t\tArezzo\t\t\t\t\tAR\n\t\t\t\tAsti\t\t\t\t\tAT\n\t\t\t\tAvellino\t\t\t\tAV\n\t\t\t\tBari\t\t\t\t\tBA\n\t\t\t\tBergamo\t\t\t\t\tBG\n\t\t\t\tBiella\t\t\t\t\tBI\n\t\t\t\tBelluno\t\t\t\t\tBL\n\t\t\t\tBenevento\t\t\t\tBN\n\t\t\t\tBologna\t\t\t\t\tBO\n\t\t\t\tBrindisi\t\t\t\tBR\n\t\t\t\tBrescia\t\t\t\t\tBS\n\t\t\t\tBarletta-Andria-Trani\tBT\n\t\t\t\tBolzano\t\t\t\t\tBZ\n\t\t\t\tCagliari\t\t\t\tCA\n\t\t\t\tCampobasso\t\t\t\tCB\n\t\t\t\tCaserta\t\t\t\t\tCE\n\t\t\t\tChieti\t\t\t\t\tCH\n\t\t\t\tCarbonia-Iglessias\t\tCI\n\t\t\t\tCaltanissetta\t\t\tCL\n\t\t\t\tCuneo\t\t\t\t\tCN\n\t\t\t\tComo\t\t\t\t\tCO\n\t\t\t\tCremona\t\t\t\t\tCR\n\t\t\t\tCosenza\t\t\t\t\tCS\n\t\t\t\tCatania\t\t\t\t\tCT\n\t\t\t\tCatanzaro\t\t\t\tCZ\n\t\t\t\tEnna\t\t\t\t\tEN\n\t\t\t\tForl\xec-Cesena\t\t\tFC\n\t\t\t\tFerrara\t\t\t\t\tFE\n\t\t\t\tFoggia\t\t\t\t\tFG\n\t\t\t\tFirenze\t\t\t\t\tFI\n\t\t\t\tFermo\t\t\t\t\tFM\n\t\t\t\tFrosinone\t\t\t\tFR\n\t\t\t\tGenova\t\t\t\t\tGE\n\t\t\t\tGorizia\t\t\t\t\tGO\n\t\t\t\tGrosseto\t\t\t\tGR\n\t\t\t\tImperia\t\t\t\t\tIM\n\t\t\t\tIsernia\t\t\t\t\tIS\n\t\t\t\tCrotone\t\t\t\t\tKR\n\t\t\t\tLecco\t\t\t\t\tLC\n\t\t\t\tLecce\t\t\t\t\tLE\n\t\t\t\tLivorno\t\t\t\t\tLI\n\t\t\t\tLodi\t\t\t\t\tLO\n\t\t\t\tLatina\t\t\t\t\tLT\n\t\t\t\tLucca\t\t\t\t\tLU\n\t\t\t\tMonza e Brianza\t\t\tMB\n\t\t\t\tMacerata\t\t\t\tMC\n\t\t\t\tMessina\t\t\t\t\tME\n\t\t\t\tMilano\t\t\t\t\tMI\n\t\t\t\tMantova\t\t\t\t\tMN\n\t\t\t\tModena\t\t\t\t\tMO\n\t\t\t\tMassa e Carrara\t\t\tMS\n\t\t\t\tMatera\t\t\t\t\tMT\n\t\t\t\tNapoli\t\t\t\t\tNA\n\t\t\t\tNovara\t\t\t\t\tNO\n\t\t\t\tNuoro\t\t\t\t\tNU\n\t\t\t\tOgliastra\t\t\t\tOG\n\t\t\t\tOristano\t\t\t\tOR\n\t\t\t\tOlbia-Tempio\t\t\tOT\n\t\t\t\tPalermo\t\t\t\t\tPA\n\t\t\t\tPiacenza\t\t\t\tPC\n\t\t\t\tPadova\t\t\t\t\tPD\n\t\t\t\tPescara\t\t\t\t\tPE\n\t\t\t\tPerugia\t\t\t\t\tPG\n\t\t\t\tPisa\t\t\t\t\tPI\n\t\t\t\tPordenone\t\t\t\tPN\n\t\t\t\tPrato\t\t\t\t\tPO\n\t\t\t\tParma\t\t\t\t\tPR\n\t\t\t\tPistoia\t\t\t\t\tPT\n\t\t\t\tPesaro e Urbino\t\t\tPU\n\t\t\t\tPavia\t\t\t\t\tPV\n\t\t\t\tPotenza\t\t\t\t\tPZ\n\t\t\t\tRavenna\t\t\t\t\tRA\n\t\t\t\tReggio Calabria\t\t\tRC\n\t\t\t\tReggio Emilia\t\t\tRE\n\t\t\t\tRagusa\t\t\t\t\tRG\n\t\t\t\tRieti\t\t\t\t\tRI\n\t\t\t\tRoma\t\t\t\t\tRM\n\t\t\t\tRimini\t\t\t\t\tRN\n\t\t\t\tRovigo\t\t\t\t\tRO\n\t\t\t\tSalerno\t\t\t\t\tSA\n\t\t\t\tiena\t\t\t\t\tSI\n\t\t\t\tSondrio\t\t\t\t\tSO\n\t\t\t\tLa Spezia\t\t\t\tSP\n\t\t\t\tSiracusa\t\t\t\tSR\n\t\t\t\tSassari\t\t\t\t\tSS\n\t\t\t\tSavona\t\t\t\t\tSV\n\t\t\t\tTaranto\t\t\t\t\tTA\n\t\t\t\tTeramo\t\t\t\t\tTE\n\t\t\t\tTrento \t\t\t\t\tTN\n\t\t\t\tTorino\t\t\t\t\tTO\n\t\t\t\tTrapani\t\t\t\t\tTP\n\t\t\t\tTerni\t\t\t\t\tTR\n\t\t\t\tTrieste\t\t\t\t\tTS\n\t\t\t\tTreviso\t\t\t\t\tTV\n\t\t\t\tUdine\t\t\t\t\tUD\n\t\t\t\tVarese\t\t\t\t\tVA\n\t\t\t\tVerbano-Cusio-Ossola\tVB\n\t\t\t\tVercelli\t\t\t\tVC\n\t\t\t\tVenezia\t\t\t\t\tVE\n\t\t\t\tVicenza\t\t\t\t\tVI\n\t\t\t\tVerona\t\t\t\t\tVR\n\t\t\t\tMedio Campidano\t\t\tVS\n\t\t\t\tViterbo\t\t\t\t\tVT\n\t\t\t\tVibo Valentia\t\t\tVV\n\t\t\t\n\t\t\t"


ProvincieItaliane._CF_enumeration = pyxb.binding.facets.CF_enumeration(
    value_datatype=ProvincieItaliane, enum_prefix=None)
ProvincieItaliane.AG = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='AG', tag='AG')
ProvincieItaliane.AL = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='AL', tag='AL')
ProvincieItaliane.AN = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='AN', tag='AN')
ProvincieItaliane.AO = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='AO', tag='AO')
ProvincieItaliane.AP = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='AP', tag='AP')
ProvincieItaliane.AQ = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='AQ', tag='AQ')
ProvincieItaliane.AR = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='AR', tag='AR')
ProvincieItaliane.AT = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='AT', tag='AT')
ProvincieItaliane.AV = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='AV', tag='AV')
ProvincieItaliane.BA = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='BA', tag='BA')
ProvincieItaliane.BG = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='BG', tag='BG')
ProvincieItaliane.BI = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='BI', tag='BI')
ProvincieItaliane.BL = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='BL', tag='BL')
ProvincieItaliane.BN = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='BN', tag='BN')
ProvincieItaliane.BO = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='BO', tag='BO')
ProvincieItaliane.BR = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='BR', tag='BR')
ProvincieItaliane.BS = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='BS', tag='BS')
ProvincieItaliane.BT = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='BT', tag='BT')
ProvincieItaliane.BZ = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='BZ', tag='BZ')
ProvincieItaliane.CA = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='CA', tag='CA')
ProvincieItaliane.CB = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='CB', tag='CB')
ProvincieItaliane.CE = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='CE', tag='CE')
ProvincieItaliane.CH = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='CH', tag='CH')
ProvincieItaliane.CI = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='CI', tag='CI')
ProvincieItaliane.CL = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='CL', tag='CL')
ProvincieItaliane.CN = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='CN', tag='CN')
ProvincieItaliane.CO = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='CO', tag='CO')
ProvincieItaliane.CR = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='CR', tag='CR')
ProvincieItaliane.CS = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='CS', tag='CS')
ProvincieItaliane.CT = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='CT', tag='CT')
ProvincieItaliane.CZ = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='CZ', tag='CZ')
ProvincieItaliane.EN = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='EN', tag='EN')
ProvincieItaliane.FC = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='FC', tag='FC')
ProvincieItaliane.FE = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='FE', tag='FE')
ProvincieItaliane.FG = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='FG', tag='FG')
ProvincieItaliane.FI = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='FI', tag='FI')
ProvincieItaliane.FM = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='FM', tag='FM')
ProvincieItaliane.FR = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='FR', tag='FR')
ProvincieItaliane.GE = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='GE', tag='GE')
ProvincieItaliane.GO = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='GO', tag='GO')
ProvincieItaliane.GR = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='GR', tag='GR')
ProvincieItaliane.IM = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='IM', tag='IM')
ProvincieItaliane.IS = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='IS', tag='IS')
ProvincieItaliane.KR = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='KR', tag='KR')
ProvincieItaliane.LC = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='LC', tag='LC')
ProvincieItaliane.LE = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='LE', tag='LE')
ProvincieItaliane.LI = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='LI', tag='LI')
ProvincieItaliane.LO = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='LO', tag='LO')
ProvincieItaliane.LT = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='LT', tag='LT')
ProvincieItaliane.LU = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='LU', tag='LU')
ProvincieItaliane.MB = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='MB', tag='MB')
ProvincieItaliane.MC = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='MC', tag='MC')
ProvincieItaliane.ME = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='ME', tag='ME')
ProvincieItaliane.MI = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='MI', tag='MI')
ProvincieItaliane.MN = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='MN', tag='MN')
ProvincieItaliane.MO = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='MO', tag='MO')
ProvincieItaliane.MS = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='MS', tag='MS')
ProvincieItaliane.MT = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='MT', tag='MT')
ProvincieItaliane.NA = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='NA', tag='NA')
ProvincieItaliane.NO = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='NO', tag='NO')
ProvincieItaliane.NU = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='NU', tag='NU')
ProvincieItaliane.OG = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='OG', tag='OG')
ProvincieItaliane.OR = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='OR', tag='OR')
ProvincieItaliane.OT = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='OT', tag='OT')
ProvincieItaliane.PA = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='PA', tag='PA')
ProvincieItaliane.PC = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='PC', tag='PC')
ProvincieItaliane.PD = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='PD', tag='PD')
ProvincieItaliane.PE = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='PE', tag='PE')
ProvincieItaliane.PG = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='PG', tag='PG')
ProvincieItaliane.PI = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='PI', tag='PI')
ProvincieItaliane.PN = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='PN', tag='PN')
ProvincieItaliane.PO = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='PO', tag='PO')
ProvincieItaliane.PR = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='PR', tag='PR')
ProvincieItaliane.PT = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='PT', tag='PT')
ProvincieItaliane.PU = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='PU', tag='PU')
ProvincieItaliane.PV = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='PV', tag='PV')
ProvincieItaliane.PZ = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='PZ', tag='PZ')
ProvincieItaliane.RA = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='RA', tag='RA')
ProvincieItaliane.RC = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='RC', tag='RC')
ProvincieItaliane.RE = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='RE', tag='RE')
ProvincieItaliane.RG = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='RG', tag='RG')
ProvincieItaliane.RI = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='RI', tag='RI')
ProvincieItaliane.RM = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='RM', tag='RM')
ProvincieItaliane.RN = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='RN', tag='RN')
ProvincieItaliane.RO = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='RO', tag='RO')
ProvincieItaliane.SA = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='SA', tag='SA')
ProvincieItaliane.SI = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='SI', tag='SI')
ProvincieItaliane.SO = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='SO', tag='SO')
ProvincieItaliane.SP = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='SP', tag='SP')
ProvincieItaliane.SR = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='SR', tag='SR')
ProvincieItaliane.SS = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='SS', tag='SS')
ProvincieItaliane.SV = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='SV', tag='SV')
ProvincieItaliane.TA = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='TA', tag='TA')
ProvincieItaliane.TE = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='TE', tag='TE')
ProvincieItaliane.TN = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='TN', tag='TN')
ProvincieItaliane.TO = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='TO', tag='TO')
ProvincieItaliane.TP = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='TP', tag='TP')
ProvincieItaliane.TR = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='TR', tag='TR')
ProvincieItaliane.TS = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='TS', tag='TS')
ProvincieItaliane.TV = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='TV', tag='TV')
ProvincieItaliane.UD = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='UD', tag='UD')
ProvincieItaliane.VA = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='VA', tag='VA')
ProvincieItaliane.VB = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='VB', tag='VB')
ProvincieItaliane.VC = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='VC', tag='VC')
ProvincieItaliane.VE = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='VE', tag='VE')
ProvincieItaliane.VI = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='VI', tag='VI')
ProvincieItaliane.VR = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='VR', tag='VR')
ProvincieItaliane.VS = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='VS', tag='VS')
ProvincieItaliane.VT = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='VT', tag='VT')
ProvincieItaliane.VV = ProvincieItaliane._CF_enumeration.addEnumeration(
    unicode_value='VV', tag='VV')
ProvincieItaliane._InitializeFacetMap(ProvincieItaliane._CF_enumeration)
Namespace.addCategoryObject(
    'typeBinding', 'ProvincieItaliane', ProvincieItaliane)

# Atomic simple type:
# {urn:www.agenziaentrate.gov.it:specificheTecniche:common}ProvincieCroate


class ProvincieCroate (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ProvincieCroate')
    _XSDLocation = pyxb.utils.utility.Location(
        '../data/common/typesProvincie_v3.xsd', 261, 1)
    _Documentation = None


ProvincieCroate._CF_enumeration = pyxb.binding.facets.CF_enumeration(
    value_datatype=ProvincieCroate, enum_prefix=None)
ProvincieCroate.FU = ProvincieCroate._CF_enumeration.addEnumeration(
    unicode_value='FU', tag='FU')
ProvincieCroate.PL = ProvincieCroate._CF_enumeration.addEnumeration(
    unicode_value='PL', tag='PL')
ProvincieCroate.ZA = ProvincieCroate._CF_enumeration.addEnumeration(
    unicode_value='ZA', tag='ZA')
ProvincieCroate._InitializeFacetMap(ProvincieCroate._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'ProvincieCroate', ProvincieCroate)

# Atomic simple type:
# {urn:www.agenziaentrate.gov.it:specificheTecniche:common}Estero


class Estero (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Estero')
    _XSDLocation = pyxb.utils.utility.Location(
        '../data/common/typesProvincie_v3.xsd', 280, 1)
    _Documentation = None


Estero._CF_enumeration = pyxb.binding.facets.CF_enumeration(
    value_datatype=Estero, enum_prefix=None)
Estero.EE = Estero._CF_enumeration.addEnumeration(unicode_value='EE', tag='EE')
Estero._InitializeFacetMap(Estero._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'Estero', Estero)

# Union simple type: {urn:www.agenziaentrate.gov.it:specificheTecniche:common}PR_Type
# superclasses pyxb.binding.datatypes.anySimpleType


class PRType (pyxb.binding.basis.STD_union):

    """Tipo semplice costituito dalle sigle delle provincie italiane in vigore."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PR_Type')
    _XSDLocation = pyxb.utils.utility.Location(
        '../data/common/typesProvincie_v3.xsd', 12, 1)
    _Documentation = 'Tipo semplice costituito dalle sigle delle provincie italiane in vigore.'

    _MemberTypes = (ProvincieItaliane, )


PRType._CF_pattern = pyxb.binding.facets.CF_pattern()
PRType._CF_enumeration = pyxb.binding.facets.CF_enumeration(
    value_datatype=PRType)
PRType.AG = 'AG'                                 # originally ProvincieItaliane.AG
PRType.AL = 'AL'                                 # originally ProvincieItaliane.AL
PRType.AN = 'AN'                                 # originally ProvincieItaliane.AN
PRType.AO = 'AO'                                 # originally ProvincieItaliane.AO
PRType.AP = 'AP'                                 # originally ProvincieItaliane.AP
PRType.AQ = 'AQ'                                 # originally ProvincieItaliane.AQ
PRType.AR = 'AR'                                 # originally ProvincieItaliane.AR
PRType.AT = 'AT'                                 # originally ProvincieItaliane.AT
PRType.AV = 'AV'                                 # originally ProvincieItaliane.AV
PRType.BA = 'BA'                                 # originally ProvincieItaliane.BA
PRType.BG = 'BG'                                 # originally ProvincieItaliane.BG
PRType.BI = 'BI'                                 # originally ProvincieItaliane.BI
PRType.BL = 'BL'                                 # originally ProvincieItaliane.BL
PRType.BN = 'BN'                                 # originally ProvincieItaliane.BN
PRType.BO = 'BO'                                 # originally ProvincieItaliane.BO
PRType.BR = 'BR'                                 # originally ProvincieItaliane.BR
PRType.BS = 'BS'                                 # originally ProvincieItaliane.BS
PRType.BT = 'BT'                                 # originally ProvincieItaliane.BT
PRType.BZ = 'BZ'                                 # originally ProvincieItaliane.BZ
PRType.CA = 'CA'                                 # originally ProvincieItaliane.CA
PRType.CB = 'CB'                                 # originally ProvincieItaliane.CB
PRType.CE = 'CE'                                 # originally ProvincieItaliane.CE
PRType.CH = 'CH'                                 # originally ProvincieItaliane.CH
PRType.CI = 'CI'                                 # originally ProvincieItaliane.CI
PRType.CL = 'CL'                                 # originally ProvincieItaliane.CL
PRType.CN = 'CN'                                 # originally ProvincieItaliane.CN
PRType.CO = 'CO'                                 # originally ProvincieItaliane.CO
PRType.CR = 'CR'                                 # originally ProvincieItaliane.CR
PRType.CS = 'CS'                                 # originally ProvincieItaliane.CS
PRType.CT = 'CT'                                 # originally ProvincieItaliane.CT
PRType.CZ = 'CZ'                                 # originally ProvincieItaliane.CZ
PRType.EN = 'EN'                                 # originally ProvincieItaliane.EN
PRType.FC = 'FC'                                 # originally ProvincieItaliane.FC
PRType.FE = 'FE'                                 # originally ProvincieItaliane.FE
PRType.FG = 'FG'                                 # originally ProvincieItaliane.FG
PRType.FI = 'FI'                                 # originally ProvincieItaliane.FI
PRType.FM = 'FM'                                 # originally ProvincieItaliane.FM
PRType.FR = 'FR'                                 # originally ProvincieItaliane.FR
PRType.GE = 'GE'                                 # originally ProvincieItaliane.GE
PRType.GO = 'GO'                                 # originally ProvincieItaliane.GO
PRType.GR = 'GR'                                 # originally ProvincieItaliane.GR
PRType.IM = 'IM'                                 # originally ProvincieItaliane.IM
PRType.IS = 'IS'                                 # originally ProvincieItaliane.IS
PRType.KR = 'KR'                                 # originally ProvincieItaliane.KR
PRType.LC = 'LC'                                 # originally ProvincieItaliane.LC
PRType.LE = 'LE'                                 # originally ProvincieItaliane.LE
PRType.LI = 'LI'                                 # originally ProvincieItaliane.LI
PRType.LO = 'LO'                                 # originally ProvincieItaliane.LO
PRType.LT = 'LT'                                 # originally ProvincieItaliane.LT
PRType.LU = 'LU'                                 # originally ProvincieItaliane.LU
PRType.MB = 'MB'                                 # originally ProvincieItaliane.MB
PRType.MC = 'MC'                                 # originally ProvincieItaliane.MC
PRType.ME = 'ME'                                 # originally ProvincieItaliane.ME
PRType.MI = 'MI'                                 # originally ProvincieItaliane.MI
PRType.MN = 'MN'                                 # originally ProvincieItaliane.MN
PRType.MO = 'MO'                                 # originally ProvincieItaliane.MO
PRType.MS = 'MS'                                 # originally ProvincieItaliane.MS
PRType.MT = 'MT'                                 # originally ProvincieItaliane.MT
PRType.NA = 'NA'                                 # originally ProvincieItaliane.NA
PRType.NO = 'NO'                                 # originally ProvincieItaliane.NO
PRType.NU = 'NU'                                 # originally ProvincieItaliane.NU
PRType.OG = 'OG'                                 # originally ProvincieItaliane.OG
PRType.OR = 'OR'                                 # originally ProvincieItaliane.OR
PRType.OT = 'OT'                                 # originally ProvincieItaliane.OT
PRType.PA = 'PA'                                 # originally ProvincieItaliane.PA
PRType.PC = 'PC'                                 # originally ProvincieItaliane.PC
PRType.PD = 'PD'                                 # originally ProvincieItaliane.PD
PRType.PE = 'PE'                                 # originally ProvincieItaliane.PE
PRType.PG = 'PG'                                 # originally ProvincieItaliane.PG
PRType.PI = 'PI'                                 # originally ProvincieItaliane.PI
PRType.PN = 'PN'                                 # originally ProvincieItaliane.PN
PRType.PO = 'PO'                                 # originally ProvincieItaliane.PO
PRType.PR = 'PR'                                 # originally ProvincieItaliane.PR
PRType.PT = 'PT'                                 # originally ProvincieItaliane.PT
PRType.PU = 'PU'                                 # originally ProvincieItaliane.PU
PRType.PV = 'PV'                                 # originally ProvincieItaliane.PV
PRType.PZ = 'PZ'                                 # originally ProvincieItaliane.PZ
PRType.RA = 'RA'                                 # originally ProvincieItaliane.RA
PRType.RC = 'RC'                                 # originally ProvincieItaliane.RC
PRType.RE = 'RE'                                 # originally ProvincieItaliane.RE
PRType.RG = 'RG'                                 # originally ProvincieItaliane.RG
PRType.RI = 'RI'                                 # originally ProvincieItaliane.RI
PRType.RM = 'RM'                                 # originally ProvincieItaliane.RM
PRType.RN = 'RN'                                 # originally ProvincieItaliane.RN
PRType.RO = 'RO'                                 # originally ProvincieItaliane.RO
PRType.SA = 'SA'                                 # originally ProvincieItaliane.SA
PRType.SI = 'SI'                                 # originally ProvincieItaliane.SI
PRType.SO = 'SO'                                 # originally ProvincieItaliane.SO
PRType.SP = 'SP'                                 # originally ProvincieItaliane.SP
PRType.SR = 'SR'                                 # originally ProvincieItaliane.SR
PRType.SS = 'SS'                                 # originally ProvincieItaliane.SS
PRType.SV = 'SV'                                 # originally ProvincieItaliane.SV
PRType.TA = 'TA'                                 # originally ProvincieItaliane.TA
PRType.TE = 'TE'                                 # originally ProvincieItaliane.TE
PRType.TN = 'TN'                                 # originally ProvincieItaliane.TN
PRType.TO = 'TO'                                 # originally ProvincieItaliane.TO
PRType.TP = 'TP'                                 # originally ProvincieItaliane.TP
PRType.TR = 'TR'                                 # originally ProvincieItaliane.TR
PRType.TS = 'TS'                                 # originally ProvincieItaliane.TS
PRType.TV = 'TV'                                 # originally ProvincieItaliane.TV
PRType.UD = 'UD'                                 # originally ProvincieItaliane.UD
PRType.VA = 'VA'                                 # originally ProvincieItaliane.VA
PRType.VB = 'VB'                                 # originally ProvincieItaliane.VB
PRType.VC = 'VC'                                 # originally ProvincieItaliane.VC
PRType.VE = 'VE'                                 # originally ProvincieItaliane.VE
PRType.VI = 'VI'                                 # originally ProvincieItaliane.VI
PRType.VR = 'VR'                                 # originally ProvincieItaliane.VR
PRType.VS = 'VS'                                 # originally ProvincieItaliane.VS
PRType.VT = 'VT'                                 # originally ProvincieItaliane.VT
PRType.VV = 'VV'                                 # originally ProvincieItaliane.VV
PRType._InitializeFacetMap(PR_Type._CF_pattern,
                            PRType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'PR_Type', PRType)

# Union simple type: {urn:www.agenziaentrate.gov.it:specificheTecniche:common}PN_Type
# superclasses pyxb.binding.datatypes.anySimpleType


class PNType (pyxb.binding.basis.STD_union):

    """Tipo semplice costituito dalle sigle delle provincie italiane in vigore,  dalle sigle delle provincie croate di Fiume, Pola e Zara e dalla sigla “EE” che indica un paese estero."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PN_Type')
    _XSDLocation = pyxb.utils.utility.Location(
        '../data/common/typesProvincie_v3.xsd', 18, 1)
    _Documentation = 'Tipo semplice costituito dalle sigle delle provincie italiane in vigore,  dalle sigle delle provincie croate di Fiume, Pola e Zara e dalla sigla \u201cEE\u201d che indica un paese estero.'

    _MemberTypes = (ProvincieItaliane, ProvincieCroate, Estero, )


PNType._CF_pattern = pyxb.binding.facets.CF_pattern()
PNType._CF_enumeration = pyxb.binding.facets.CF_enumeration(
    value_datatype=PNType)
PNType.AG = 'AG'                                 # originally ProvincieItaliane.AG
PNType.AL = 'AL'                                 # originally ProvincieItaliane.AL
PNType.AN = 'AN'                                 # originally ProvincieItaliane.AN
PNType.AO = 'AO'                                 # originally ProvincieItaliane.AO
PNType.AP = 'AP'                                 # originally ProvincieItaliane.AP
PNType.AQ = 'AQ'                                 # originally ProvincieItaliane.AQ
PNType.AR = 'AR'                                 # originally ProvincieItaliane.AR
PNType.AT = 'AT'                                 # originally ProvincieItaliane.AT
PNType.AV = 'AV'                                 # originally ProvincieItaliane.AV
PNType.BA = 'BA'                                 # originally ProvincieItaliane.BA
PNType.BG = 'BG'                                 # originally ProvincieItaliane.BG
PNType.BI = 'BI'                                 # originally ProvincieItaliane.BI
PNType.BL = 'BL'                                 # originally ProvincieItaliane.BL
PNType.BN = 'BN'                                 # originally ProvincieItaliane.BN
PNType.BO = 'BO'                                 # originally ProvincieItaliane.BO
PNType.BR = 'BR'                                 # originally ProvincieItaliane.BR
PNType.BS = 'BS'                                 # originally ProvincieItaliane.BS
PNType.BT = 'BT'                                 # originally ProvincieItaliane.BT
PNType.BZ = 'BZ'                                 # originally ProvincieItaliane.BZ
PNType.CA = 'CA'                                 # originally ProvincieItaliane.CA
PNType.CB = 'CB'                                 # originally ProvincieItaliane.CB
PNType.CE = 'CE'                                 # originally ProvincieItaliane.CE
PNType.CH = 'CH'                                 # originally ProvincieItaliane.CH
PNType.CI = 'CI'                                 # originally ProvincieItaliane.CI
PNType.CL = 'CL'                                 # originally ProvincieItaliane.CL
PNType.CN = 'CN'                                 # originally ProvincieItaliane.CN
PNType.CO = 'CO'                                 # originally ProvincieItaliane.CO
PNType.CR = 'CR'                                 # originally ProvincieItaliane.CR
PNType.CS = 'CS'                                 # originally ProvincieItaliane.CS
PNType.CT = 'CT'                                 # originally ProvincieItaliane.CT
PNType.CZ = 'CZ'                                 # originally ProvincieItaliane.CZ
PNType.EN = 'EN'                                 # originally ProvincieItaliane.EN
PNType.FC = 'FC'                                 # originally ProvincieItaliane.FC
PNType.FE = 'FE'                                 # originally ProvincieItaliane.FE
PNType.FG = 'FG'                                 # originally ProvincieItaliane.FG
PNType.FI = 'FI'                                 # originally ProvincieItaliane.FI
PNType.FM = 'FM'                                 # originally ProvincieItaliane.FM
PNType.FR = 'FR'                                 # originally ProvincieItaliane.FR
PNType.GE = 'GE'                                 # originally ProvincieItaliane.GE
PNType.GO = 'GO'                                 # originally ProvincieItaliane.GO
PNType.GR = 'GR'                                 # originally ProvincieItaliane.GR
PNType.IM = 'IM'                                 # originally ProvincieItaliane.IM
PNType.IS = 'IS'                                 # originally ProvincieItaliane.IS
PNType.KR = 'KR'                                 # originally ProvincieItaliane.KR
PNType.LC = 'LC'                                 # originally ProvincieItaliane.LC
PNType.LE = 'LE'                                 # originally ProvincieItaliane.LE
PNType.LI = 'LI'                                 # originally ProvincieItaliane.LI
PNType.LO = 'LO'                                 # originally ProvincieItaliane.LO
PNType.LT = 'LT'                                 # originally ProvincieItaliane.LT
PNType.LU = 'LU'                                 # originally ProvincieItaliane.LU
PNType.MB = 'MB'                                 # originally ProvincieItaliane.MB
PNType.MC = 'MC'                                 # originally ProvincieItaliane.MC
PNType.ME = 'ME'                                 # originally ProvincieItaliane.ME
PNType.MI = 'MI'                                 # originally ProvincieItaliane.MI
PNType.MN = 'MN'                                 # originally ProvincieItaliane.MN
PNType.MO = 'MO'                                 # originally ProvincieItaliane.MO
PNType.MS = 'MS'                                 # originally ProvincieItaliane.MS
PNType.MT = 'MT'                                 # originally ProvincieItaliane.MT
PNType.NA = 'NA'                                 # originally ProvincieItaliane.NA
PNType.NO = 'NO'                                 # originally ProvincieItaliane.NO
PNType.NU = 'NU'                                 # originally ProvincieItaliane.NU
PNType.OG = 'OG'                                 # originally ProvincieItaliane.OG
PNType.OR = 'OR'                                 # originally ProvincieItaliane.OR
PNType.OT = 'OT'                                 # originally ProvincieItaliane.OT
PNType.PA = 'PA'                                 # originally ProvincieItaliane.PA
PNType.PC = 'PC'                                 # originally ProvincieItaliane.PC
PNType.PD = 'PD'                                 # originally ProvincieItaliane.PD
PNType.PE = 'PE'                                 # originally ProvincieItaliane.PE
PNType.PG = 'PG'                                 # originally ProvincieItaliane.PG
PNType.PI = 'PI'                                 # originally ProvincieItaliane.PI
PNType.PN = 'PN'                                 # originally ProvincieItaliane.PN
PNType.PO = 'PO'                                 # originally ProvincieItaliane.PO
PNType.PR = 'PR'                                 # originally ProvincieItaliane.PR
PNType.PT = 'PT'                                 # originally ProvincieItaliane.PT
PNType.PU = 'PU'                                 # originally ProvincieItaliane.PU
PNType.PV = 'PV'                                 # originally ProvincieItaliane.PV
PNType.PZ = 'PZ'                                 # originally ProvincieItaliane.PZ
PNType.RA = 'RA'                                 # originally ProvincieItaliane.RA
PNType.RC = 'RC'                                 # originally ProvincieItaliane.RC
PNType.RE = 'RE'                                 # originally ProvincieItaliane.RE
PNType.RG = 'RG'                                 # originally ProvincieItaliane.RG
PNType.RI = 'RI'                                 # originally ProvincieItaliane.RI
PNType.RM = 'RM'                                 # originally ProvincieItaliane.RM
PNType.RN = 'RN'                                 # originally ProvincieItaliane.RN
PNType.RO = 'RO'                                 # originally ProvincieItaliane.RO
PNType.SA = 'SA'                                 # originally ProvincieItaliane.SA
PNType.SI = 'SI'                                 # originally ProvincieItaliane.SI
PNType.SO = 'SO'                                 # originally ProvincieItaliane.SO
PNType.SP = 'SP'                                 # originally ProvincieItaliane.SP
PNType.SR = 'SR'                                 # originally ProvincieItaliane.SR
PNType.SS = 'SS'                                 # originally ProvincieItaliane.SS
PNType.SV = 'SV'                                 # originally ProvincieItaliane.SV
PNType.TA = 'TA'                                 # originally ProvincieItaliane.TA
PNType.TE = 'TE'                                 # originally ProvincieItaliane.TE
PNType.TN = 'TN'                                 # originally ProvincieItaliane.TN
PNType.TO = 'TO'                                 # originally ProvincieItaliane.TO
PNType.TP = 'TP'                                 # originally ProvincieItaliane.TP
PNType.TR = 'TR'                                 # originally ProvincieItaliane.TR
PNType.TS = 'TS'                                 # originally ProvincieItaliane.TS
PNType.TV = 'TV'                                 # originally ProvincieItaliane.TV
PNType.UD = 'UD'                                 # originally ProvincieItaliane.UD
PNType.VA = 'VA'                                 # originally ProvincieItaliane.VA
PNType.VB = 'VB'                                 # originally ProvincieItaliane.VB
PNType.VC = 'VC'                                 # originally ProvincieItaliane.VC
PNType.VE = 'VE'                                 # originally ProvincieItaliane.VE
PNType.VI = 'VI'                                 # originally ProvincieItaliane.VI
PNType.VR = 'VR'                                 # originally ProvincieItaliane.VR
PNType.VS = 'VS'                                 # originally ProvincieItaliane.VS
PNType.VT = 'VT'                                 # originally ProvincieItaliane.VT
PNType.VV = 'VV'                                 # originally ProvincieItaliane.VV
PNType.FU = 'FU'                                 # originally ProvincieCroate.FU
PNType.PL = 'PL'                                 # originally ProvincieCroate.PL
PNType.ZA = 'ZA'                                 # originally ProvincieCroate.ZA
PNType.EE = 'EE'                                 # originally Estero.EE
PNType._InitializeFacetMap(PN_Type._CF_pattern,
                            PNType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'PN_Type', PNType)

# Union simple type: {urn:www.agenziaentrate.gov.it:specificheTecniche:common}PE_Type
# superclasses pyxb.binding.datatypes.anySimpleType


class PEType (pyxb.binding.basis.STD_union):

    """Tipo semplice costituito dalle sigle delle provincie italiane in vigore e dalla sigla “EE” che indica un paese estero."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PE_Type')
    _XSDLocation = pyxb.utils.utility.Location(
        '../data/common/typesProvincie_v3.xsd', 24, 1)
    _Documentation = 'Tipo semplice costituito dalle sigle delle provincie italiane in vigore e dalla sigla \u201cEE\u201d che indica un paese estero.'

    _MemberTypes = (ProvincieItaliane, Estero, )


PEType._CF_pattern = pyxb.binding.facets.CF_pattern()
PEType._CF_enumeration = pyxb.binding.facets.CF_enumeration(
    value_datatype=PEType)
PEType.AG = 'AG'                                 # originally ProvincieItaliane.AG
PEType.AL = 'AL'                                 # originally ProvincieItaliane.AL
PEType.AN = 'AN'                                 # originally ProvincieItaliane.AN
PEType.AO = 'AO'                                 # originally ProvincieItaliane.AO
PEType.AP = 'AP'                                 # originally ProvincieItaliane.AP
PEType.AQ = 'AQ'                                 # originally ProvincieItaliane.AQ
PEType.AR = 'AR'                                 # originally ProvincieItaliane.AR
PEType.AT = 'AT'                                 # originally ProvincieItaliane.AT
PEType.AV = 'AV'                                 # originally ProvincieItaliane.AV
PEType.BA = 'BA'                                 # originally ProvincieItaliane.BA
PEType.BG = 'BG'                                 # originally ProvincieItaliane.BG
PEType.BI = 'BI'                                 # originally ProvincieItaliane.BI
PEType.BL = 'BL'                                 # originally ProvincieItaliane.BL
PEType.BN = 'BN'                                 # originally ProvincieItaliane.BN
PEType.BO = 'BO'                                 # originally ProvincieItaliane.BO
PEType.BR = 'BR'                                 # originally ProvincieItaliane.BR
PEType.BS = 'BS'                                 # originally ProvincieItaliane.BS
PEType.BT = 'BT'                                 # originally ProvincieItaliane.BT
PEType.BZ = 'BZ'                                 # originally ProvincieItaliane.BZ
PEType.CA = 'CA'                                 # originally ProvincieItaliane.CA
PEType.CB = 'CB'                                 # originally ProvincieItaliane.CB
PEType.CE = 'CE'                                 # originally ProvincieItaliane.CE
PEType.CH = 'CH'                                 # originally ProvincieItaliane.CH
PEType.CI = 'CI'                                 # originally ProvincieItaliane.CI
PEType.CL = 'CL'                                 # originally ProvincieItaliane.CL
PEType.CN = 'CN'                                 # originally ProvincieItaliane.CN
PEType.CO = 'CO'                                 # originally ProvincieItaliane.CO
PEType.CR = 'CR'                                 # originally ProvincieItaliane.CR
PEType.CS = 'CS'                                 # originally ProvincieItaliane.CS
PEType.CT = 'CT'                                 # originally ProvincieItaliane.CT
PEType.CZ = 'CZ'                                 # originally ProvincieItaliane.CZ
PEType.EN = 'EN'                                 # originally ProvincieItaliane.EN
PEType.FC = 'FC'                                 # originally ProvincieItaliane.FC
PEType.FE = 'FE'                                 # originally ProvincieItaliane.FE
PEType.FG = 'FG'                                 # originally ProvincieItaliane.FG
PEType.FI = 'FI'                                 # originally ProvincieItaliane.FI
PEType.FM = 'FM'                                 # originally ProvincieItaliane.FM
PEType.FR = 'FR'                                 # originally ProvincieItaliane.FR
PEType.GE = 'GE'                                 # originally ProvincieItaliane.GE
PEType.GO = 'GO'                                 # originally ProvincieItaliane.GO
PEType.GR = 'GR'                                 # originally ProvincieItaliane.GR
PEType.IM = 'IM'                                 # originally ProvincieItaliane.IM
PEType.IS = 'IS'                                 # originally ProvincieItaliane.IS
PEType.KR = 'KR'                                 # originally ProvincieItaliane.KR
PEType.LC = 'LC'                                 # originally ProvincieItaliane.LC
PEType.LE = 'LE'                                 # originally ProvincieItaliane.LE
PEType.LI = 'LI'                                 # originally ProvincieItaliane.LI
PEType.LO = 'LO'                                 # originally ProvincieItaliane.LO
PEType.LT = 'LT'                                 # originally ProvincieItaliane.LT
PEType.LU = 'LU'                                 # originally ProvincieItaliane.LU
PEType.MB = 'MB'                                 # originally ProvincieItaliane.MB
PEType.MC = 'MC'                                 # originally ProvincieItaliane.MC
PEType.ME = 'ME'                                 # originally ProvincieItaliane.ME
PEType.MI = 'MI'                                 # originally ProvincieItaliane.MI
PEType.MN = 'MN'                                 # originally ProvincieItaliane.MN
PEType.MO = 'MO'                                 # originally ProvincieItaliane.MO
PEType.MS = 'MS'                                 # originally ProvincieItaliane.MS
PEType.MT = 'MT'                                 # originally ProvincieItaliane.MT
PEType.NA = 'NA'                                 # originally ProvincieItaliane.NA
PEType.NO = 'NO'                                 # originally ProvincieItaliane.NO
PEType.NU = 'NU'                                 # originally ProvincieItaliane.NU
PEType.OG = 'OG'                                 # originally ProvincieItaliane.OG
PEType.OR = 'OR'                                 # originally ProvincieItaliane.OR
PEType.OT = 'OT'                                 # originally ProvincieItaliane.OT
PEType.PA = 'PA'                                 # originally ProvincieItaliane.PA
PEType.PC = 'PC'                                 # originally ProvincieItaliane.PC
PEType.PD = 'PD'                                 # originally ProvincieItaliane.PD
PEType.PE = 'PE'                                 # originally ProvincieItaliane.PE
PEType.PG = 'PG'                                 # originally ProvincieItaliane.PG
PEType.PI = 'PI'                                 # originally ProvincieItaliane.PI
PEType.PN = 'PN'                                 # originally ProvincieItaliane.PN
PEType.PO = 'PO'                                 # originally ProvincieItaliane.PO
PEType.PR = 'PR'                                 # originally ProvincieItaliane.PR
PEType.PT = 'PT'                                 # originally ProvincieItaliane.PT
PEType.PU = 'PU'                                 # originally ProvincieItaliane.PU
PEType.PV = 'PV'                                 # originally ProvincieItaliane.PV
PEType.PZ = 'PZ'                                 # originally ProvincieItaliane.PZ
PEType.RA = 'RA'                                 # originally ProvincieItaliane.RA
PEType.RC = 'RC'                                 # originally ProvincieItaliane.RC
PEType.RE = 'RE'                                 # originally ProvincieItaliane.RE
PEType.RG = 'RG'                                 # originally ProvincieItaliane.RG
PEType.RI = 'RI'                                 # originally ProvincieItaliane.RI
PEType.RM = 'RM'                                 # originally ProvincieItaliane.RM
PEType.RN = 'RN'                                 # originally ProvincieItaliane.RN
PEType.RO = 'RO'                                 # originally ProvincieItaliane.RO
PEType.SA = 'SA'                                 # originally ProvincieItaliane.SA
PEType.SI = 'SI'                                 # originally ProvincieItaliane.SI
PEType.SO = 'SO'                                 # originally ProvincieItaliane.SO
PEType.SP = 'SP'                                 # originally ProvincieItaliane.SP
PEType.SR = 'SR'                                 # originally ProvincieItaliane.SR
PEType.SS = 'SS'                                 # originally ProvincieItaliane.SS
PEType.SV = 'SV'                                 # originally ProvincieItaliane.SV
PEType.TA = 'TA'                                 # originally ProvincieItaliane.TA
PEType.TE = 'TE'                                 # originally ProvincieItaliane.TE
PEType.TN = 'TN'                                 # originally ProvincieItaliane.TN
PEType.TO = 'TO'                                 # originally ProvincieItaliane.TO
PEType.TP = 'TP'                                 # originally ProvincieItaliane.TP
PEType.TR = 'TR'                                 # originally ProvincieItaliane.TR
PEType.TS = 'TS'                                 # originally ProvincieItaliane.TS
PEType.TV = 'TV'                                 # originally ProvincieItaliane.TV
PEType.UD = 'UD'                                 # originally ProvincieItaliane.UD
PEType.VA = 'VA'                                 # originally ProvincieItaliane.VA
PEType.VB = 'VB'                                 # originally ProvincieItaliane.VB
PEType.VC = 'VC'                                 # originally ProvincieItaliane.VC
PEType.VE = 'VE'                                 # originally ProvincieItaliane.VE
PEType.VI = 'VI'                                 # originally ProvincieItaliane.VI
PEType.VR = 'VR'                                 # originally ProvincieItaliane.VR
PEType.VS = 'VS'                                 # originally ProvincieItaliane.VS
PEType.VT = 'VT'                                 # originally ProvincieItaliane.VT
PEType.VV = 'VV'                                 # originally ProvincieItaliane.VV
PEType.EE = 'EE'                                 # originally Estero.EE
PEType._InitializeFacetMap(PE_Type._CF_pattern,
                            PEType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'PE_Type', PEType)

# Complex type
# {urn:www.agenziaentrate.gov.it:specificheTecniche:common}Documento_Type
# with content type EMPTY


class DocumentoType (pyxb.binding.basis.complexTypeDefinition):
    """Documento trasmesso"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Documento_Type')
    _XSDLocation = pyxb.utils.utility.Location(
        '../data/common/fornitura_v3.xsd', 21, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Attribute identificativo uses Python identifier identificativo
    __identificativo = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(
        None, 'identificativo'), 'identificativo', '__urnwww_agenziaentrate_gov_itspecificheTecnichecommon_Documento_Type_identificativo', IdentificativoType, required=True)
    __identificativo._DeclarationLocation = pyxb.utils.utility.Location(
        '../data/common/fornitura_v3.xsd', 25, 2)
    __identificativo._UseLocation = pyxb.utils.utility.Location(
        '../data/common/fornitura_v3.xsd', 25, 2)

    identificativo = property(__identificativo.value,
                              __identificativo.set, None, None)

    _ElementMap.update({

    })
    _AttributeMap.update({
        __identificativo.name(): __identificativo
    })


Namespace.addCategoryObject('typeBinding', 'Documento_Type', DocumentoType)


Documento = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Documento'), DocumentoType, abstract=pyxb.binding.datatypes.boolean(
    1), location=pyxb.utils.utility.Location('../data/common/fornitura_v3.xsd', 20, 1))
Namespace.addCategoryObject(
    'elementBinding', Documento.name().localName(), Documento)
