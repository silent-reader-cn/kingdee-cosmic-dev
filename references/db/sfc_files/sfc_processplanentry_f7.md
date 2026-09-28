# 工序计划分录F7-sfc_processplanentry_f7

## 工序计划分录F7-主表 t_sfc_processplanentry

- **表名称：** 工序计划分录F7-主表
- **表名：** t_sfc_processplanentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 单据编号 | int8 | 64 |  | √ | 0 | 工序计划F7 sfc_processplan_f7 |
| 2 | freworksection | freworksection | varchar | 1000 |  | √ | ' ' |  |
| 3 | frelationid | 代码生成id(关联id) | int8 | 64 |  | √ | 0 | 代码生成id(关联id) |
| 4 | fislastprocess | 末序 | bpchar | 1 |  | √ | '0' | 末序 |
| 5 | fprocessqty | 工序数量 | numeric | 23 | 10 | √ | 0 | 工序数量 |
| 6 | fprocesscontrolcode | 工序控制码 | int8 | 64 |  | √ | 0 | 工序控制码 mpdm_processcontrolcode |
| 7 | fsequencetype | 工序序列类型 | bpchar | 1 |  | √ | ' ' | 工序序列类型,枚举: A :并行序列 B :返工序列 C :主干序列 |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | freportsbqty | freportsbqty | numeric | 23 | 10 | √ | 0 |  |
| 10 | fprocessroutid | fprocessroutid | int8 | 64 |  | √ | 0 |  |
| 11 | fbegintime | fbegintime | timestamp | 0 |  |  | null |  |
| 12 | fupprocesstype | fupprocesstype | varchar | 10 |  | √ | ' ' |  |
| 13 | fisfirstprocess | 首序 | bpchar | 1 |  | √ | '0' | 首序 |
| 14 | flowerqty | flowerqty | numeric | 23 | 10 | √ | 0 |  |
| 15 | fprocessdepartid | 加工车间 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 16 | freworkplanqty | freworkplanqty | numeric | 23 | 10 | √ | 0 |  |
| 17 | fprocessnumber | 工序号 | int4 | 32 |  | √ | 0 | 工序号 |
| 18 | ftobereworkedqty | ftobereworkedqty | numeric | 23 | 10 | √ | 0 |  |
| 19 | fprocessinfocode | 工序编码 | varchar | 30 |  | √ | ' ' | 工序编码 |
| 20 | fprocessunit | 工序单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 21 | freworkedqty | freworkedqty | numeric | 23 | 10 | √ | 0 |  |
| 22 | fhigherqty | fhigherqty | numeric | 23 | 10 | √ | 0 |  |
| 23 | fprocessorg | 加工组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 24 | fplanbegintime | 计划开工日期 | timestamp | 0 |  |  | null | 计划开工日期 |
| 25 | freworksequence | freworksequence | int8 | 64 |  | √ | 0 |  |
| 26 | fsumquaqyt | fsumquaqyt | numeric | 23 | 10 | √ | 0 |  |
| 27 | fplanendtime1 | fplanendtime1 | timestamp | 0 |  |  | null |  |
| 28 | fpromethod | 加工类型 | varchar | 10 |  | √ | ' ' | 加工类型,枚举: 1 :厂内加工 2 :内协加工 3 :委外加工 |
| 29 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 30 | fsumstockwastqty | fsumstockwastqty | numeric | 23 | 10 | √ | 0 |  |
| 31 | fprocesssequence | 序列号 | int8 | 64 |  | √ | 0 | 序列号 |
| 32 | fintoqty | fintoqty | numeric | 23 | 10 | √ | 0 |  |
| 33 | fbasebsqty | 基本批量 | numeric | 23 | 10 | √ | 0 | 基本批量 |
| 34 | fupprocessid | fupprocessid | varchar | 1000 |  | √ | ' ' |  |
| 35 | freportmethod | 汇报控制 | varchar | 10 |  | √ | ' ' | 汇报控制,枚举: no :不汇报 must :必须汇报 |
| 36 | frevoveryqty | frevoveryqty | numeric | 23 | 10 | √ | 0 |  |
| 37 | fprocessinstructions | 工序说明 | varchar | 512 |  | √ | ' ' | 工序说明 |
| 38 | foutsourcedqty | foutsourcedqty | numeric | 23 | 10 | √ | 0 |  |
| 39 | fprocesscode | 工序编码 | int8 | 64 |  | √ | 0 | 标准工序 mpdm_normprocess |
| 40 | fsumworkwastqty | fsumworkwastqty | numeric | 23 | 10 | √ | 0 |  |
| 41 | freportordercontrol | 汇报顺序控制 | bpchar | 1 |  | √ | ' ' | 汇报顺序控制,枚举: A :不控制 B :警告 C :严格控制 |
| 42 | fnextprocessid | 下工序id | varchar | 1000 |  | √ | ' ' | 下工序id |
| 43 | fcompleteqty | fcompleteqty | numeric | 23 | 10 | √ | 0 |  |
| 44 | fismilestone | 里程牌工序 | bpchar | 1 |  | √ | '0' | 里程牌工序 |
| 45 | fplanbegintime1 | fplanbegintime1 | timestamp | 0 |  |  | null |  |
| 46 | fprocesstatus | 工序状态 | varchar | 10 |  | √ | ' ' | 工序状态,枚举: A :计划 B :下达 C :开工 D :完工 |
| 47 | fplanendtime | 计划完工日期 | timestamp | 0 |  |  | null | 计划完工日期 |
| 48 | fismainprocess | 主工序 | bpchar | 1 |  | √ | '0' | 主工序 |
| 49 | fendtime | fendtime | timestamp | 0 |  |  | null |  |
| 50 | fprocesscenter | 工作中心 | int8 | 64 |  | √ | 0 | 工作中心 sfc_workcenter |
| 51 | freworkprocesses | freworkprocesses | int8 | 64 |  | √ | 0 |  |

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
| 2 | fintoqty | fintoqty | numeric | 23 | 10 | √ | 0 |  |
| 3 | fsumworkwastbaseqty | fsumworkwastbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 4 | fsumcompleteqty | fsumcompleteqty | numeric | 23 | 10 | √ | 0 |  |
| 5 | freportsbqty | 汇报选单数量 | numeric | 23 | 10 | √ | 0 | 汇报选单数量 |
| 6 | ftobereworkedbaseqty | ftobereworkedbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 7 | freportmethod | freportmethod | varchar | 10 |  | √ | ' ' |  |
| 8 | fsumcompletebaseqty | fsumcompletebaseqty | numeric | 23 | 10 | √ | 0 |  |
| 9 | fheadunitfactor | 表头单位换算系数 | int4 | 32 |  | √ | 0 | 表头单位换算系数 |
| 10 | fbegintime | fbegintime | timestamp | 0 |  |  | null |  |
| 11 | fsumworkwastproqty | fsumworkwastproqty | numeric | 23 | 10 | √ | 0 |  |
| 12 | frevoveryqty | frevoveryqty | numeric | 23 | 10 | √ | 0 |  |
| 13 | ftobeinspectproqty | ftobeinspectproqty | numeric | 23 | 10 | √ | 0 |  |
| 14 | foutsourcedqty | 委外发出数量 | numeric | 23 | 10 | √ | 0 | 委外发出数量 |
| 15 | flowerqty | flowerqty | numeric | 23 | 10 | √ | 0 |  |
| 16 | fsumquabaseqyt | fsumquabaseqyt | numeric | 23 | 10 | √ | 0 |  |
| 17 | freworkdrawqty | 返工选单数量 | numeric | 23 | 10 | √ | 0 | 返工选单数量 |
| 18 | fouttoqty | fouttoqty | numeric | 23 | 10 | √ | 0 |  |
| 19 | fsumworkwastqty | 累计工废数量 | numeric | 23 | 10 | √ | 0 | 累计工废数量 |
| 20 | ftobereworkedqty | 待返工数量 | numeric | 23 | 10 | √ | 0 | 待返工数量 |
| 21 | fsumstockwastproqty | fsumstockwastproqty | numeric | 23 | 10 | √ | 0 |  |
| 22 | ftobereworkedproqty | ftobereworkedproqty | numeric | 23 | 10 | √ | 0 |  |
| 23 | ftobeinspectqty | ftobeinspectqty | numeric | 23 | 10 | √ | 0 |  |
| 24 | fcompletebaseqty | fcompletebaseqty | numeric | 23 | 10 | √ | 0 |  |
| 25 | ftobeinsbaseqty | ftobeinsbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 26 | foutsourcedsbqty | 委外发出选单数量 | numeric | 23 | 10 | √ | 0 | 委外发出选单数量 |
| 27 | fprounitfactor | 工序单位换算系数 | int4 | 32 |  | √ | 0 | 工序单位换算系数 |
| 28 | freworkedqty | freworkedqty | numeric | 23 | 10 | √ | 0 |  |
| 29 | fhigherqty | 汇报上限 | numeric | 23 | 10 | √ | 0 | 汇报上限 |
| 30 | fsumstockwastbaseqty | fsumstockwastbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 31 | fcompleteproqty | fcompleteproqty | numeric | 23 | 10 | √ | 0 |  |
| 32 | fcompleteqty | 完工数量 | numeric | 23 | 10 | √ | 0 | 完工数量 |
| 33 | ftransfersbqty | ftransfersbqty | numeric | 23 | 10 | √ | 0 |  |
| 34 | fsumquaproqyt | fsumquaproqyt | numeric | 23 | 10 | √ | 0 |  |
| 35 | fsumquaqyt | 累计合格数量 | numeric | 23 | 10 | √ | 0 | 累计合格数量 |
| 36 | freportdownlimit | freportdownlimit | numeric | 23 | 10 | √ | 0 |  |
| 37 | fendtime | fendtime | timestamp | 0 |  |  | null |  |
| 38 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 39 | fsumstockwastqty | 累计料废数量 | numeric | 23 | 10 | √ | 0 | 累计料废数量 |
| 40 | freportupperlimit | 汇报上限允差（%） | numeric | 23 | 10 | √ | 0 | 汇报上限允差（%） |
| 41 | fyetreworkedqty | 已返工数量 | numeric | 23 | 10 | √ | 0 | 已返工数量 |

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
| 2 | fpurchasegroupid | fpurchasegroupid | int8 | 64 |  | √ | 0 |  |
| 3 | foutreworkproqty | foutreworkproqty | numeric | 23 | 10 | √ | 0 |  |
| 4 | finreworkproqty | finreworkproqty | numeric | 23 | 10 | √ | 0 |  |
| 5 | foutsourcepriceandtax | 委外含税单价 | numeric | 23 | 10 | √ | 0 | 委外含税单价 |
| 6 | fworkwasteprice | 工废单价 | numeric | 23 | 10 | √ | 0 | 工废单价 |
| 7 | foutreworkqty | foutreworkqty | numeric | 23 | 10 | √ | 0 |  |
| 8 | finacceptqty | finacceptqty | numeric | 23 | 10 | √ | 0 |  |
| 9 | fchargeunitid | 计价单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 10 | finsendmenuqty | 内协发出选单数量 | numeric | 23 | 10 | √ | 0 | 内协发出选单数量 |
| 11 | fpurchaseorgid | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 12 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 13 | finreworkbaseqty | finreworkbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 14 | fscrapwasteprice | 料废单价 | numeric | 23 | 10 | √ | 0 | 料废单价 |
| 15 | fworkwastepriceandtax | 工废含税单价 | numeric | 23 | 10 | √ | 0 | 工废含税单价 |
| 16 | foutreworkbaseqty | foutreworkbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 17 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 18 | finsendqty | 内协发出数量 | numeric | 23 | 10 | √ | 0 | 内协发出数量 |
| 19 | fscrapwastepriceandtax | 料废含税单价 | numeric | 23 | 10 | √ | 0 | 料废含税单价 |
| 20 | finreworkqty | finreworkqty | numeric | 23 | 10 | √ | 0 |  |
| 21 | foutsourceprice | 委外单价 | numeric | 23 | 10 | √ | 0 | 委外单价 |
| 22 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 23 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |

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
| 2 | finspectuserid | 质检员 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fproinspect | 工序检验 | bpchar | 1 |  | √ | '0' | 工序检验 |
| 4 | finspectplan | 检验方案 | int8 | 64 |  | √ | 0 | 检验方案 qcbd_inspectpro |
| 5 | finspectdepid | 质检部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | finspectorg | 质检组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

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
| 2 | fispal | fispal | bpchar | 1 |  | √ | '0' |  |
| 3 | fraactivityreport | 准备活动人工*汇报活动量公式 | int8 | 64 |  | √ | 0 | 活动公式 mpdm_activityformula |
| 4 | fwamreportqty | 加工活动机器汇报数量 | numeric | 23 | 10 | √ | 0 | 加工活动机器汇报数量 |
| 5 | fsumwamplanqty | 加工活动机器计划活动总量 | numeric | 23 | 10 | √ | 0 | 加工活动机器计划活动总量 |
| 6 | fpamreportqty | 准备活动机器活动汇报数量 | numeric | 23 | 10 | √ | 0 | 准备活动机器活动汇报数量 |
| 7 | fispam | fispam | bpchar | 1 |  | √ | '0' |  |
| 8 | frmactivityreport | 准备活动机器*汇报活动量公式 | int8 | 64 |  | √ | 0 | 活动公式 mpdm_activityformula |
| 9 | fpmpformulaid | fpmpformulaid | int8 | 64 |  | √ | 0 |  |
| 10 | frapformulaid | frapformulaid | int8 | 64 |  | √ | 0 |  |
| 11 | frmresource | frmresource | int8 | 64 |  | √ | 0 |  |
| 12 | fwalplanqty | 加工活动人工计划数量 | numeric | 23 | 10 | √ | 0 | 加工活动人工计划数量 |
| 13 | fraresource | fraresource | int8 | 64 |  | √ | 0 |  |
| 14 | frmpformulaid | frmpformulaid | int8 | 64 |  | √ | 0 |  |
| 15 | fpamunit | 准备活动机器单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 16 | fpmactivityreport | 加工活动机器*汇报活动量公式 | int8 | 64 |  | √ | 0 | 活动公式 mpdm_activityformula |
| 17 | fwalreportqty | 加工活动人工汇报数量 | numeric | 23 | 10 | √ | 0 | 加工活动人工汇报数量 |
| 18 | fsumwalplanqty | 加工活动人工计划活动总量 | numeric | 23 | 10 | √ | 0 | 加工活动人工计划活动总量 |
| 19 | fiswal | fiswal | bpchar | 1 |  | √ | '0' |  |
| 20 | fiswam | fiswam | bpchar | 1 |  | √ | '0' |  |
| 21 | fpalplanqty | 准备活动人工计划数量 | numeric | 23 | 10 | √ | 0 | 准备活动人工计划数量 |
| 22 | fpamplanqty | 准备活动机器计划数量 | numeric | 23 | 10 | √ | 0 | 准备活动机器计划数量 |
| 23 | funitfield | 准备活动人工单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 24 | fpalreportqty | 准备活动人工活动汇报数量 | numeric | 23 | 10 | √ | 0 | 准备活动人工活动汇报数量 |
| 25 | fwalunit | 加工活动人工单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 26 | fpaactivityreport | 加工活动人工*汇报活动量公式 | int8 | 64 |  | √ | 0 | 活动公式 mpdm_activityformula |
| 27 | fpapformulaid | fpapformulaid | int8 | 64 |  | √ | 0 |  |
| 28 | fwamplanqty | 加工活动机器计划数量 | numeric | 23 | 10 | √ | 0 | 加工活动机器计划数量 |
| 29 | fiscomeup3 | fiscomeup3 | bpchar | 1 |  | √ | '0' |  |
| 30 | fwamunit | 加工活动机器单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 31 | fiscomeup4 | fiscomeup4 | bpchar | 1 |  | √ | '0' |  |
| 32 | fiscomeup1 | fiscomeup1 | bpchar | 1 |  | √ | '0' |  |
| 33 | fsumpamplanqty | 准备活动机器计划活动总量 | numeric | 23 | 10 | √ | 0 | 准备活动机器计划活动总量 |
| 34 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 35 | fiscomeup2 | fiscomeup2 | bpchar | 1 |  | √ | '0' |  |
| 36 | fsumpalplanqty | 准备活动人工计划活动总量 | numeric | 23 | 10 | √ | 0 | 准备活动人工计划活动总量 |
| 37 | fpmresource | fpmresource | int8 | 64 |  | √ | 0 |  |
| 38 | fparesource | fparesource | int8 | 64 |  | √ | 0 |  |

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
| 3 | fomresource | fomresource | int8 | 64 |  | √ | 0 |  |
| 4 | fpalplanqty8 | 其他活动二人工计划数量 | numeric | 23 | 10 | √ | 0 | 其他活动二人工计划数量 |
| 5 | foaresource | foaresource | int8 | 64 |  | √ | 0 |  |
| 6 | ftmresource | ftmresource | int8 | 64 |  | √ | 0 |  |
| 7 | fompformulaid | fompformulaid | int8 | 64 |  | √ | 0 |  |
| 8 | fsumoomplanqty | 其他活动一机器计划活动总量 | numeric | 23 | 10 | √ | 0 | 其他活动一机器计划活动总量 |
| 9 | foapformulaid | foapformulaid | int8 | 64 |  | √ | 0 |  |
| 10 | foaactivityreport | 其他活动一人工*汇报活动量公式 | int8 | 64 |  | √ | 0 | 活动公式 mpdm_activityformula |
| 11 | fsumoopplanqty | 其他活动一人工计划活动总量 | numeric | 23 | 10 | √ | 0 | 其他活动一人工计划活动总量 |
| 12 | fpamreportqty8 | 其他活动二人工汇报数量 | numeric | 23 | 10 | √ | 0 | 其他活动二人工汇报数量 |
| 13 | ftaresource | ftaresource | int8 | 64 |  | √ | 0 |  |
| 14 | funitfield8 | 其他活动二人工单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 15 | fpamreportqty4 | 其他活动二机器汇报数量 | numeric | 23 | 10 | √ | 0 | 其他活动二机器汇报数量 |
| 16 | ftmactivityreport | 其他活动二机器*汇报活动量公式 | int8 | 64 |  | √ | 0 | 活动公式 mpdm_activityformula |
| 17 | funitfield3 | 其他活动一机器单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 18 | fpalplanqty7 | 其他活动一人工计划数量 | numeric | 23 | 10 | √ | 0 | 其他活动一人工计划数量 |
| 19 | ftapformulaid | ftapformulaid | int8 | 64 |  | √ | 0 |  |
| 20 | fpalplanqty4 | 其他活动二机器计划数量 | numeric | 23 | 10 | √ | 0 | 其他活动二机器计划数量 |
| 21 | fomactivityreport | 其他活动一机器*汇报活动量公式 | int8 | 64 |  | √ | 0 | 活动公式 mpdm_activityformula |
| 22 | fpamreportqty3 | 其他活动一机器汇报数量 | numeric | 23 | 10 | √ | 0 | 其他活动一机器汇报数量 |
| 23 | ftaactivityreport | 其他活动二人工*汇报活动量公式 | int8 | 64 |  | √ | 0 | 活动公式 mpdm_activityformula |
| 24 | funitfield7 | 其他活动一人工单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 25 | fpalplanqty3 | 其他活动一机器计划数量 | numeric | 23 | 10 | √ | 0 | 其他活动一机器计划数量 |
| 26 | funitfield4 | 其他活动二机器单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 27 | fsumospplanqty | 其他活动二人工计划活动总量 | numeric | 23 | 10 | √ | 0 | 其他活动二人工计划活动总量 |
| 28 | ftmpformulaid | ftmpformulaid | int8 | 64 |  | √ | 0 |  |
| 29 | fispal4 | fispal4 | bpchar | 1 |  | √ | '0' |  |
| 30 | fiscomeup14 | fiscomeup14 | bpchar | 1 |  | √ | '0' |  |
| 31 | fispal3 | fispal3 | bpchar | 1 |  | √ | '0' |  |
| 32 | fsumosmplanqty | 其他活动二机器计划活动总量 | numeric | 23 | 10 | √ | 0 | 其他活动二机器计划活动总量 |
| 33 | fiscomeup13 | fiscomeup13 | bpchar | 1 |  | √ | '0' |  |
| 34 | fispal8 | fispal8 | bpchar | 1 |  | √ | '0' |  |
| 35 | fiscomeup18 | fiscomeup18 | bpchar | 1 |  | √ | '0' |  |
| 36 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 37 | fispal7 | fispal7 | bpchar | 1 |  | √ | '0' |  |
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
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_plane_l_id |  | fentryid |
| 2 | pk_t_sfc_processplanentry_l |  | fpkid |
