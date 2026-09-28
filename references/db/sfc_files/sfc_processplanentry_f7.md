# 工序计划分录F7-sfc_processplanentry_f7

## 工序计划分录F7-主表 t_sfc_processplanentry

- **表名称：** 工序计划分录F7-主表
- **表名：** t_sfc_processplanentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 单据编号 | int8 | 64 |  | √ | 0 | [工序计划F7 sfc_processplan_f7](../sfc_files/sfc_processplan_f7.md) |
| 2 | freworksection | freworksection | varchar | 1000 |  | √ | ' ' |  |
| 3 | frelationid | 代码生成id(关联id) | int8 | 64 |  | √ | 0 | 代码生成id(关联id) |
| 4 | ftransinrelationids | 转入工序relationid | varchar | 500 |  | √ | ' ' | 转入工序relationid |
| 5 | fislastprocess | 末序 | bpchar | 1 |  | √ | '0' | 末序 |
| 6 | fprocessqty | 工序数量 | numeric | 23 | 10 | √ | 0 | 工序数量 |
| 7 | fprocesscontrolcode | 工序控制码 | int8 | 64 |  | √ | 0 | [工序控制码 mpdm_processcontrolcode](../mpdm_files/mpdm_processcontrolcode.md) |
| 8 | fsequencetype | 序列类型 | bpchar | 1 |  | √ | ' ' | 序列类型,枚举: A :并行序列 B :返工序列 C :主干序列 |
| 9 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 10 | freportsbqty | freportsbqty | numeric | 23 | 10 | √ | 0 |  |
| 11 | fprocessroutid | fprocessroutid | int8 | 64 |  | √ | 0 |  |
| 12 | fbegintime | fbegintime | timestamp | 0 |  |  | null |  |
| 13 | fclosetime | fclosetime | timestamp | 0 |  |  | null |  |
| 14 | fupprocesstype | fupprocesstype | varchar | 10 |  | √ | ' ' |  |
| 15 | fsendworktype | fsendworktype | bpchar | 1 |  | √ | ' ' |  |
| 16 | fisfirstprocess | 首序 | bpchar | 1 |  | √ | '0' | 首序 |
| 17 | flowerqty | flowerqty | numeric | 23 | 10 | √ | 0 |  |
| 18 | fprocessdepartid | 加工车间 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 19 | freworkplanqty | freworkplanqty | numeric | 23 | 10 | √ | 0 |  |
| 20 | fprocessnumber | 工序号 | int4 | 32 |  | √ | 0 | 工序号 |
| 21 | ftobereworkedqty | ftobereworkedqty | numeric | 23 | 10 | √ | 0 |  |
| 22 | fprocessinfocode | 工序编码 | varchar | 30 |  | √ | ' ' | 工序编码 |
| 23 | fsequenceremark | fsequenceremark | varchar | 512 |  | √ | ' ' |  |
| 24 | fprocessunit | 工序单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 25 | freworkedqty | freworkedqty | numeric | 23 | 10 | √ | 0 |  |
| 26 | fhigherqty | fhigherqty | numeric | 23 | 10 | √ | 0 |  |
| 27 | ftransoutrelationids | ftransoutrelationids | varchar | 500 |  | √ | ' ' |  |
| 28 | fprocessorg | 加工组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 29 | fplanbegintime | 计划开工日期 | timestamp | 0 |  |  | null | 计划开工日期 |
| 30 | freworksequence | freworksequence | int8 | 64 |  | √ | 0 |  |
| 31 | fsumquaqyt | fsumquaqyt | numeric | 23 | 10 | √ | 0 |  |
| 32 | fplanendtime1 | fplanendtime1 | timestamp | 0 |  |  | null |  |
| 33 | fpromethod | 加工类型 | varchar | 10 |  | √ | ' ' | 加工类型,枚举: 1 :厂内加工 2 :内协加工 3 :委外加工 |
| 34 | fiskeyprocess | fiskeyprocess | bpchar | 1 |  | √ | '0' |  |
| 35 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 36 | fsumstockwastqty | fsumstockwastqty | numeric | 23 | 10 | √ | 0 |  |
| 37 | freworkmode | 返工方式 | bpchar | 1 |  | √ | ' ' | 返工方式,枚举: A :直接返工 B :返工序列 |
| 38 | fprocesssequence | 工序序列 | int8 | 64 |  | √ | 0 | 工序序列 |
| 39 | fjobtype | 作业类型 | bpchar | 1 |  | √ | ' ' | 作业类型,枚举: A :团队作业 B :个人作业 |
| 40 | fintoqty | fintoqty | numeric | 23 | 10 | √ | 0 |  |
| 41 | fbasebsqty | 基本批量 | numeric | 23 | 10 | √ | 0 | 基本批量 |
| 42 | fupprocessid | fupprocessid | varchar | 1000 |  | √ | ' ' |  |
| 43 | freportmethod | 汇报控制 | varchar | 10 |  | √ | ' ' | 汇报控制,枚举: no :不汇报 must :必须汇报 |
| 44 | frevoveryqty | frevoveryqty | numeric | 23 | 10 | √ | 0 |  |
| 45 | fprocessinstructions | 工序说明 | varchar | 512 |  | √ | ' ' | 工序说明 |
| 46 | foutsourcedqty | foutsourcedqty | numeric | 23 | 10 | √ | 0 |  |
| 47 | fprocesscode | 工序编码 | int8 | 64 |  | √ | 0 | [标准工序 mpdm_normprocess](../mpdm_files/mpdm_normprocess.md) |
| 48 | fsumworkwastqty | fsumworkwastqty | numeric | 23 | 10 | √ | 0 |  |
| 49 | fclosebeforestatus | fclosebeforestatus | varchar | 10 |  | √ | ' ' |  |
| 50 | freportordercontrol | 汇报顺序控制 | bpchar | 1 |  | √ | ' ' | 汇报顺序控制,枚举: A :不控制 B :警告 C :严格控制 |
| 51 | fnextprocessid | 下工序id | varchar | 1000 |  | √ | ' ' | 下工序id |
| 52 | freportqty | freportqty | numeric | 23 | 10 | √ | 0 |  |
| 53 | fcompleteqty | fcompleteqty | numeric | 23 | 10 | √ | 0 |  |
| 54 | fismilestone | 里程牌工序 | bpchar | 1 |  | √ | '0' | 里程牌工序 |
| 55 | fplanbegintime1 | fplanbegintime1 | timestamp | 0 |  |  | null |  |
| 56 | ftransinqty | ftransinqty | numeric | 23 | 10 | √ | 0 |  |
| 57 | fprocesstatus | 工序状态 | varchar | 10 |  | √ | ' ' | 工序状态,枚举: A :计划 B :下达 C :开工 D :完工 E :关闭 |
| 58 | fplanendtime | 计划完工日期 | timestamp | 0 |  |  | null | 计划完工日期 |
| 59 | ftransinunitid | ftransinunitid | int8 | 64 |  | √ | 0 |  |
| 60 | fismainprocess | 主工序 | bpchar | 1 |  | √ | '0' | 主工序 |
| 61 | fendtime | fendtime | timestamp | 0 |  |  | null |  |
| 62 | fprocesscenter | 工作中心 | int8 | 64 |  | √ | 0 | [工作中心 sfc_workcenter](../mpdm_files/sfc_workcenter.md) |
| 63 | freworkprocesses | freworkprocesses | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_processplanentry |  | fentryid |
| 2 | idx_sfc_plane_id |  | fid |

---

## 工序计划分录F7-分表 t_sfc_processplanentry_c

- **表名称：** 工序计划分录F7-分表
- **表名：** t_sfc_processplanentry_c

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freworkoutproqty | freworkoutproqty | numeric | 23 | 10 | √ | 0 |  |
| 3 | fdamageproqty | fdamageproqty | numeric | 23 | 10 | √ | 0 |  |
| 4 | fsumcompleteqty | fsumcompleteqty | numeric | 23 | 10 | √ | 0 |  |
| 5 | freportsbqty | 汇报选单数量 | numeric | 23 | 10 | √ | 0 | 汇报选单数量 |
| 6 | fsumcompletebaseqty | fsumcompletebaseqty | numeric | 23 | 10 | √ | 0 |  |
| 7 | fheadunitfactor | 表头单位换算系数 | int4 | 32 |  | √ | 0 | 表头单位换算系数 |
| 8 | fbegintime | fbegintime | timestamp | 0 |  |  | null |  |
| 9 | finproqty | finproqty | numeric | 23 | 10 | √ | 0 |  |
| 10 | flowerqty | flowerqty | numeric | 23 | 10 | √ | 0 |  |
| 11 | fyetsendworkqty | 已派工数量 | numeric | 23 | 10 | √ | 0 | 已派工数量 |
| 12 | fsumquabaseqyt | fsumquabaseqyt | numeric | 23 | 10 | √ | 0 |  |
| 13 | finbaseqty | finbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 14 | freworkdrawqty | 返工选单数量 | numeric | 23 | 10 | √ | 0 | 返工选单数量 |
| 15 | ftobesendworkbaseqty | ftobesendworkbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 16 | fouttoqty | fouttoqty | numeric | 23 | 10 | √ | 0 |  |
| 17 | ftobereworkedqty | 待返工数量 | numeric | 23 | 10 | √ | 0 | 待返工数量 |
| 18 | ftobereworkedproqty | ftobereworkedproqty | numeric | 23 | 10 | √ | 0 |  |
| 19 | frelateinbaseqty | frelateinbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 20 | frelatereworkoutbaseqty | frelatereworkoutbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 21 | ftobeinsbaseqty | ftobeinsbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 22 | foutsourcedsbqty | 委外发出选单数量 | numeric | 23 | 10 | √ | 0 | 委外发出选单数量 |
| 23 | frelateinproqty | frelateinproqty | numeric | 23 | 10 | √ | 0 |  |
| 24 | fprounitfactor | 工序单位换算系数 | int4 | 32 |  | √ | 0 | 工序单位换算系数 |
| 25 | freworkedqty | freworkedqty | numeric | 23 | 10 | √ | 0 |  |
| 26 | fhigherqty | 汇报上限 | numeric | 23 | 10 | √ | 0 | 汇报上限 |
| 27 | fyetsendworkbaseqty | fyetsendworkbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 28 | fsumstockwastbaseqty | fsumstockwastbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 29 | fsampledestorybaseqty | fsampledestorybaseqty | numeric | 23 | 10 | √ | 0 |  |
| 30 | fsendworkstate | fsendworkstate | bpchar | 1 |  | √ | ' ' |  |
| 31 | ftransfersbqty | ftransfersbqty | numeric | 23 | 10 | √ | 0 |  |
| 32 | fsumquaproqyt | fsumquaproqyt | numeric | 23 | 10 | √ | 0 |  |
| 33 | fsumquaqyt | 累计合格数量 | numeric | 23 | 10 | √ | 0 | 累计合格数量 |
| 34 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 35 | fsumstockwastqty | 累计料废数量 | numeric | 23 | 10 | √ | 0 | 累计料废数量 |
| 36 | freportupperlimit | 汇报上限允差（%） | numeric | 23 | 10 | √ | 0 | 汇报上限允差（%） |
| 37 | freworkoutqty | freworkoutqty | numeric | 23 | 10 | √ | 0 |  |
| 38 | fintoqty | fintoqty | numeric | 23 | 10 | √ | 0 |  |
| 39 | finqty | finqty | numeric | 23 | 10 | √ | 0 |  |
| 40 | foutqty | foutqty | numeric | 23 | 10 | √ | 0 |  |
| 41 | freworkoutbaseqty | freworkoutbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 42 | frelateoutqty | frelateoutqty | numeric | 23 | 10 | √ | 0 |  |
| 43 | fsumworkwastbaseqty | fsumworkwastbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 44 | frelatereworkoutproqty | frelatereworkoutproqty | numeric | 23 | 10 | √ | 0 |  |
| 45 | fsampledestoryproqty | fsampledestoryproqty | numeric | 23 | 10 | √ | 0 |  |
| 46 | ftobereworkedbaseqty | ftobereworkedbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 47 | freportmethod | freportmethod | varchar | 10 |  | √ | ' ' |  |
| 48 | fdamagebaseqty | fdamagebaseqty | numeric | 23 | 10 | √ | 0 |  |
| 49 | fyetsendworkproqty | fyetsendworkproqty | numeric | 23 | 10 | √ | 0 |  |
| 50 | frelateoutbaseqty | frelateoutbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 51 | fsumworkwastproqty | fsumworkwastproqty | numeric | 23 | 10 | √ | 0 |  |
| 52 | frevoveryqty | frevoveryqty | numeric | 23 | 10 | √ | 0 |  |
| 53 | ftobeinspectproqty | ftobeinspectproqty | numeric | 23 | 10 | √ | 0 |  |
| 54 | foutsourcedqty | 委外发出数量 | numeric | 23 | 10 | √ | 0 | 委外发出数量 |
| 55 | ftobesendworkproqty | ftobesendworkproqty | numeric | 23 | 10 | √ | 0 |  |
| 56 | foutproqty | foutproqty | numeric | 23 | 10 | √ | 0 |  |
| 57 | frelatereworkoutqty | frelatereworkoutqty | numeric | 23 | 10 | √ | 0 |  |
| 58 | fsumworkwastqty | 累计工废数量 | numeric | 23 | 10 | √ | 0 | 累计工废数量 |
| 59 | fsumstockwastproqty | fsumstockwastproqty | numeric | 23 | 10 | √ | 0 |  |
| 60 | frelateoutproqty | frelateoutproqty | numeric | 23 | 10 | √ | 0 |  |
| 61 | frelateinqty | frelateinqty | numeric | 23 | 10 | √ | 0 |  |
| 62 | ftobeinspectqty | ftobeinspectqty | numeric | 23 | 10 | √ | 0 |  |
| 63 | fcompletebaseqty | fcompletebaseqty | numeric | 23 | 10 | √ | 0 |  |
| 64 | fsampledestoryqty | fsampledestoryqty | numeric | 23 | 10 | √ | 0 |  |
| 65 | fcompleteproqty | fcompleteproqty | numeric | 23 | 10 | √ | 0 |  |
| 66 | foutbaseqty | foutbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 67 | fcompleteqty | 完工数量 | numeric | 23 | 10 | √ | 0 | 完工数量 |
| 68 | ftobesendworkqty | 关联派工数量 | numeric | 23 | 10 | √ | 0 | 关联派工数量 |
| 69 | freportdownlimit | freportdownlimit | numeric | 23 | 10 | √ | 0 |  |
| 70 | fdamageqty | fdamageqty | numeric | 23 | 10 | √ | 0 |  |
| 71 | fendtime | fendtime | timestamp | 0 |  |  | null |  |
| 72 | fyetreworkedqty | 已返工数量 | numeric | 23 | 10 | √ | 0 | 已返工数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_processplanentry_c |  | fentryid |
| 2 | idx_sfc_plane_c_id |  | fid |

---

## 工序计划分录F7-分表 t_sfc_processplanentry_d

- **表名称：** 工序计划分录F7-分表
- **表名：** t_sfc_processplanentry_d

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxratevalue | ftaxratevalue | numeric | 23 | 10 | √ | 0 |  |
| 3 | fpurchasegroupid | fpurchasegroupid | int8 | 64 |  | √ | 0 |  |
| 4 | foutreworkproqty | foutreworkproqty | numeric | 23 | 10 | √ | 0 |  |
| 5 | finreworkproqty | finreworkproqty | numeric | 23 | 10 | √ | 0 |  |
| 6 | foutsourcepriceandtax | 委外含税单价 | numeric | 23 | 10 | √ | 0 | 委外含税单价 |
| 7 | fworkwasteprice | 工废单价 | numeric | 23 | 10 | √ | 0 | 工废单价 |
| 8 | foutreworkqty | foutreworkqty | numeric | 23 | 10 | √ | 0 |  |
| 9 | finacceptqty | finacceptqty | numeric | 23 | 10 | √ | 0 |  |
| 10 | fchargeunitid | 计价单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 11 | finsendmenuqty | 内协发出选单数量 | numeric | 23 | 10 | √ | 0 | 内协发出选单数量 |
| 12 | fpurchaseorgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 13 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 14 | finreworkbaseqty | finreworkbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 15 | fscrapwasteprice | 料废单价 | numeric | 23 | 10 | √ | 0 | 料废单价 |
| 16 | fworkwastepriceandtax | 工废含税单价 | numeric | 23 | 10 | √ | 0 | 工废含税单价 |
| 17 | foutreworkbaseqty | foutreworkbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 18 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 19 | finsendqty | 内协发出数量 | numeric | 23 | 10 | √ | 0 | 内协发出数量 |
| 20 | fscrapwastepriceandtax | 料废含税单价 | numeric | 23 | 10 | √ | 0 | 料废含税单价 |
| 21 | finreworkqty | finreworkqty | numeric | 23 | 10 | √ | 0 |  |
| 22 | foutsourceprice | 委外单价 | numeric | 23 | 10 | √ | 0 | 委外单价 |
| 23 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 24 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_processplanentry_d |  | fentryid |
| 2 | idx_sfc_plane_d_id |  | fid |

---

## 工序计划分录F7-分表 t_sfc_processplanentry_i

- **表名称：** 工序计划分录F7-分表
- **表名：** t_sfc_processplanentry_i

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffirstincontrolmode | ffirstincontrolmode | bpchar | 1 |  | √ | ' ' |  |
| 3 | fpickingstate | fpickingstate | bpchar | 1 |  | √ | ' ' |  |
| 4 | fproinspect | 工序检验 | bpchar | 1 |  | √ | '0' | 工序检验 |
| 5 | finspectschemeid | 检验方案编码 | int8 | 64 |  | √ | 0 | [检验方案 qcbd_inspectpro](../qcbd_files/qcbd_inspectpro.md) |
| 6 | ffirstinstate | 首检状态 | bpchar | 1 |  | √ | ' ' | 首检状态,枚举: A :空 B :待首检 C :首检中 D :首检完成 |
| 7 | finspectuserid | 质检员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fpatrolinstate | fpatrolinstate | bpchar | 1 |  | √ | ' ' |  |
| 9 | finspectplan | 检验方案(废弃) | int8 | 64 |  | √ | 0 | [工作中心 sfc_workcenter](../mpdm_files/sfc_workcenter.md) |
| 10 | finspectplanrowid | 检验方案分录id | int8 | 64 |  | √ | 0 | 检验方案分录id |
| 11 | ffirstinspect | 首检 | bpchar | 1 |  | √ | '0' | 首检 |
| 12 | finspectdepid | 质检部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 13 | finspectorg | 质检组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 15 | fpropickingqty | fpropickingqty | numeric | 23 | 10 | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_processplanentry_i |  | fentryid |
| 2 | idx_sfc_proplanentry_i_id |  | fid |

---

## 工序计划分录F7-分表 t_sfc_processplanentry_a

- **表名称：** 工序计划分录F7-分表
- **表名：** t_sfc_processplanentry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fispal | 准备活动人工 | bpchar | 1 |  | √ | '0' | 准备活动人工 |
| 3 | fraactivityreport | 准备活动人工*汇报活动量公式 | int8 | 64 |  | √ | 0 | [活动公式 mpdm_activityformula](../mpdm_files/mpdm_activityformula.md) |
| 4 | fwamreportqty | 加工活动机器汇报数量 | numeric | 23 | 10 | √ | 0 | 加工活动机器汇报数量 |
| 5 | fsumwamplanqty | 加工活动机器计划活动总量 | numeric | 23 | 10 | √ | 0 | 加工活动机器计划活动总量 |
| 6 | fpamreportqty | 准备活动机器活动汇报数量 | numeric | 23 | 10 | √ | 0 | 准备活动机器活动汇报数量 |
| 7 | fispam | 准备活动机器 | bpchar | 1 |  | √ | '0' | 准备活动机器 |
| 8 | frmactivityreport | 准备活动机器*汇报活动量公式 | int8 | 64 |  | √ | 0 | [活动公式 mpdm_activityformula](../mpdm_files/mpdm_activityformula.md) |
| 9 | fpmpformulaid | fpmpformulaid | int8 | 64 |  | √ | 0 |  |
| 10 | frapformulaid | frapformulaid | int8 | 64 |  | √ | 0 |  |
| 11 | frmresource | 准备活动机器*资源 | int8 | 64 |  | √ | 0 | [资源 mpdm_resourceinfo](../mpdm_files/mpdm_resourceinfo.md) |
| 12 | fwalplanqty | 加工活动人工计划数量 | numeric | 23 | 10 | √ | 0 | 加工活动人工计划数量 |
| 13 | fraresource | 准备活动人工*资源 | int8 | 64 |  | √ | 0 | [资源 mpdm_resourceinfo](../mpdm_files/mpdm_resourceinfo.md) |
| 14 | frmpformulaid | frmpformulaid | int8 | 64 |  | √ | 0 |  |
| 15 | fpamunit | 准备活动机器单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 16 | fpmactivityreport | 加工活动机器*汇报活动量公式 | int8 | 64 |  | √ | 0 | [活动公式 mpdm_activityformula](../mpdm_files/mpdm_activityformula.md) |
| 17 | fwalreportqty | 加工活动人工汇报数量 | numeric | 23 | 10 | √ | 0 | 加工活动人工汇报数量 |
| 18 | fsumwalplanqty | 加工活动人工计划活动总量 | numeric | 23 | 10 | √ | 0 | 加工活动人工计划活动总量 |
| 19 | fiswal | 加工活动人工 | bpchar | 1 |  | √ | '0' | 加工活动人工 |
| 20 | fiswam | 加工活动机器 | bpchar | 1 |  | √ | '0' | 加工活动机器 |
| 21 | fpalplanqty | 准备活动人工计划数量 | numeric | 23 | 10 | √ | 0 | 准备活动人工计划数量 |
| 22 | fpamplanqty | 准备活动机器计划数量 | numeric | 23 | 10 | √ | 0 | 准备活动机器计划数量 |
| 23 | funitfield | 准备活动人工单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 24 | fpalreportqty | 准备活动人工活动汇报数量 | numeric | 23 | 10 | √ | 0 | 准备活动人工活动汇报数量 |
| 25 | fwalunit | 加工活动人工单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 26 | fpaactivityreport | 加工活动人工*汇报活动量公式 | int8 | 64 |  | √ | 0 | [活动公式 mpdm_activityformula](../mpdm_files/mpdm_activityformula.md) |
| 27 | fpapformulaid | fpapformulaid | int8 | 64 |  | √ | 0 |  |
| 28 | fwamplanqty | 加工活动机器计划数量 | numeric | 23 | 10 | √ | 0 | 加工活动机器计划数量 |
| 29 | fiscomeup3 | fiscomeup3 | bpchar | 1 |  | √ | '0' |  |
| 30 | fwamunit | 加工活动机器单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 31 | fiscomeup4 | fiscomeup4 | bpchar | 1 |  | √ | '0' |  |
| 32 | fiscomeup1 | fiscomeup1 | bpchar | 1 |  | √ | '0' |  |
| 33 | fsumpamplanqty | 准备活动机器计划活动总量 | numeric | 23 | 10 | √ | 0 | 准备活动机器计划活动总量 |
| 34 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 35 | fiscomeup2 | fiscomeup2 | bpchar | 1 |  | √ | '0' |  |
| 36 | fsumpalplanqty | 准备活动人工计划活动总量 | numeric | 23 | 10 | √ | 0 | 准备活动人工计划活动总量 |
| 37 | fpmresource | 加工活动机器*资源 | int8 | 64 |  | √ | 0 | [资源 mpdm_resourceinfo](../mpdm_files/mpdm_resourceinfo.md) |
| 38 | fparesource | 加工活动人工*资源 | int8 | 64 |  | √ | 0 | [资源 mpdm_resourceinfo](../mpdm_files/mpdm_resourceinfo.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_plane_a_id |  | fid |
| 2 | pk_sfc_processplanentry_a |  | fentryid |

---

## 工序计划分录F7-分表 t_sfc_processplanentry_b

- **表名称：** 工序计划分录F7-分表
- **表名：** t_sfc_processplanentry_b

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpalreportqty7 | 其他活动一人工汇报数量 | numeric | 23 | 10 | √ | 0 | 其他活动一人工汇报数量 |
| 3 | fomresource | 其他活动一机器*资源 | int8 | 64 |  | √ | 0 | [资源 mpdm_resourceinfo](../mpdm_files/mpdm_resourceinfo.md) |
| 4 | fpalplanqty8 | 其他活动二人工计划数量 | numeric | 23 | 10 | √ | 0 | 其他活动二人工计划数量 |
| 5 | foaresource | 其他活动一人工*资源 | int8 | 64 |  | √ | 0 | [资源 mpdm_resourceinfo](../mpdm_files/mpdm_resourceinfo.md) |
| 6 | ftmresource | 其他活动二机器*资源 | int8 | 64 |  | √ | 0 | [资源 mpdm_resourceinfo](../mpdm_files/mpdm_resourceinfo.md) |
| 7 | fompformulaid | fompformulaid | int8 | 64 |  | √ | 0 |  |
| 8 | fsumoomplanqty | 其他活动一机器计划活动总量 | numeric | 23 | 10 | √ | 0 | 其他活动一机器计划活动总量 |
| 9 | foapformulaid | foapformulaid | int8 | 64 |  | √ | 0 |  |
| 10 | foaactivityreport | 其他活动一人工*汇报活动量公式 | int8 | 64 |  | √ | 0 | [活动公式 mpdm_activityformula](../mpdm_files/mpdm_activityformula.md) |
| 11 | fsumoopplanqty | 其他活动一人工计划活动总量 | numeric | 23 | 10 | √ | 0 | 其他活动一人工计划活动总量 |
| 12 | fpamreportqty8 | 其他活动二人工汇报数量 | numeric | 23 | 10 | √ | 0 | 其他活动二人工汇报数量 |
| 13 | ftaresource | 其他活动二人工*资源 | int8 | 64 |  | √ | 0 | [资源 mpdm_resourceinfo](../mpdm_files/mpdm_resourceinfo.md) |
| 14 | funitfield8 | 其他活动二人工单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 15 | fpamreportqty4 | 其他活动二机器汇报数量 | numeric | 23 | 10 | √ | 0 | 其他活动二机器汇报数量 |
| 16 | ftmactivityreport | 其他活动二机器*汇报活动量公式 | int8 | 64 |  | √ | 0 | [活动公式 mpdm_activityformula](../mpdm_files/mpdm_activityformula.md) |
| 17 | funitfield3 | 其他活动一机器单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 18 | fpalplanqty7 | 其他活动一人工计划数量 | numeric | 23 | 10 | √ | 0 | 其他活动一人工计划数量 |
| 19 | ftapformulaid | ftapformulaid | int8 | 64 |  | √ | 0 |  |
| 20 | fpalplanqty4 | 其他活动二机器计划数量 | numeric | 23 | 10 | √ | 0 | 其他活动二机器计划数量 |
| 21 | fomactivityreport | 其他活动一机器*汇报活动量公式 | int8 | 64 |  | √ | 0 | [活动公式 mpdm_activityformula](../mpdm_files/mpdm_activityformula.md) |
| 22 | fpamreportqty3 | 其他活动一机器汇报数量 | numeric | 23 | 10 | √ | 0 | 其他活动一机器汇报数量 |
| 23 | ftaactivityreport | 其他活动二人工*汇报活动量公式 | int8 | 64 |  | √ | 0 | [活动公式 mpdm_activityformula](../mpdm_files/mpdm_activityformula.md) |
| 24 | funitfield7 | 其他活动一人工单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 25 | fpalplanqty3 | 其他活动一机器计划数量 | numeric | 23 | 10 | √ | 0 | 其他活动一机器计划数量 |
| 26 | funitfield4 | 其他活动二机器单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 27 | fsumospplanqty | 其他活动二人工计划活动总量 | numeric | 23 | 10 | √ | 0 | 其他活动二人工计划活动总量 |
| 28 | ftmpformulaid | ftmpformulaid | int8 | 64 |  | √ | 0 |  |
| 29 | fispal4 | 其他活动二机器 | bpchar | 1 |  | √ | '0' | 其他活动二机器 |
| 30 | fiscomeup14 | fiscomeup14 | bpchar | 1 |  | √ | '0' |  |
| 31 | fispal3 | 其他活动一机器 | bpchar | 1 |  | √ | '0' | 其他活动一机器 |
| 32 | fsumosmplanqty | 其他活动二机器计划活动总量 | numeric | 23 | 10 | √ | 0 | 其他活动二机器计划活动总量 |
| 33 | fiscomeup13 | fiscomeup13 | bpchar | 1 |  | √ | '0' |  |
| 34 | fispal8 | 其他活动二人工 | bpchar | 1 |  | √ | '0' | 其他活动二人工 |
| 35 | fiscomeup18 | fiscomeup18 | bpchar | 1 |  | √ | '0' |  |
| 36 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 37 | fispal7 | 其他活动一人工 | bpchar | 1 |  | √ | '0' | 其他活动一人工 |
| 38 | fiscomeup17 | fiscomeup17 | bpchar | 1 |  | √ | '0' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_plane_b_id |  | fid |
| 2 | pk_sfc_processplanentry_b |  | fentryid |

---

## 工序计划分录F7-多语言表 t_sfc_processplanentry_l

- **表名称：** 工序计划分录F7-多语言表
- **表名：** t_sfc_processplanentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fprocessinstructions | 工序说明 | varchar | 512 |  | √ | ' ' | 工序说明 |
| 2 | fsequenceremark | fsequenceremark | varchar | 512 |  | √ | ' ' |  |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_plane_l_id |  | fentryid |
| 2 | pk_t_sfc_processplanentry_l |  | fpkid |
