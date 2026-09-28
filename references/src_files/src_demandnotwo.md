# 项目立项F7-src_demandnotwo

## 项目立项F7-分表 t_src_demand_a

- **表名称：** 项目立项F7-分表
- **表名：** t_src_demand_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdecidelink | fdecidelink | varchar | 100 |  | √ | ' ' |  |
| 3 | fdecstatus | 关联采委会状态 | bpchar | 1 |  | √ | ' ' | 关联采委会状态,枚举: A :未上报 B :已上报 C :已关联 |
| 4 | fdecisionid | 采委会决策单号 | int8 | 64 |  | √ | 0 | 采委会决策单号 src_decisionbillnotwo |
| 5 | fistemppush | fistemppush | bpchar | 1 |  | √ | '0' |  |
| 6 | fdecidenumber | fdecidenumber | varchar | 50 |  | √ | ' ' |  |
| 7 | fresultstatus | fresultstatus | bpchar | 1 |  | √ | ' ' |  |
| 8 | ftempreason | ftempreason | varchar | 255 |  | √ | ' ' |  |
| 9 | fconclusion | fconclusion | varchar | 1000 |  | √ | ' ' |  |
| 10 | fdecisiontype | fdecisiontype | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_demand_a_fid |  | fdecidenumber |
| 2 | pk_src_demand_a |  | fid |

---

## 项目立项F7-多语言表 t_src_demand_l

- **表名称：** 项目立项F7-多语言表
- **表名：** t_src_demand_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftitle | 项目立项名称 | varchar | 300 |  | √ | ' ' | 项目立项名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_demand_l |  | fpkid |
| 2 | idx_src_demand_l_flocaleid |  | fid,flocaleid |

---

## 采购组织-多选基础资料表 t_src_demandpurorg

- **表名称：** 采购组织-多选基础资料表
- **表名：** t_src_demandpurorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_demandpurorg_fid |  | fid |
| 2 | pk_src_demandpurorg |  | fpkid |
| 3 | idx_src_demandpurorg_bid |  | fbasedataid |

---

## 底盘类型-多选基础资料表 t_src_demand_chasstype

- **表名称：** 底盘类型-多选基础资料表
- **表名：** t_src_demand_chasstype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 招标辅助资料 pds_extdata |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_demand_chasstype_fid |  | fid |
| 2 | pk_src_demand_chasstype |  | fpkid |
| 3 | idx_src_demand_chasstype_bid |  | fbasedataid |

---

## 项目立项F7-主表 t_src_demand

- **表名称：** 项目立项F7-主表
- **表名：** t_src_demand

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 2 | fisproject | fisproject | bpchar | 1 |  | √ | '0' |  |
| 3 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fplace | fplace | int8 | 64 |  | √ | 0 |  |
| 5 | fsrctypeid | 寻源流程 | int8 | 64 |  | √ | 0 | 流程配置 pds_flowconfig |
| 6 | fpentitykey | fpentitykey | varchar | 50 |  | √ | ' ' |  |
| 7 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 8 | fsrcemotion | 寻源情形 | varchar | 30 |  | √ | ' ' | 寻源情形,枚举: A :新增品项首次评审 B :合同外新增物资 C :已有合同价格下调 D :产品重新选型 E :已有合同价格上浮 F :年度合同重新寻源 G :其他 |
| 9 | ftextfield | ftextfield | varchar | 50 |  | √ | ' ' |  |
| 10 | ftitle | ftitle | varchar | 300 |  | √ | ' ' |  |
| 11 | fwithvatamount | fwithvatamount | numeric | 23 | 10 | √ | 0 |  |
| 12 | forigin | forigin | bpchar | 1 |  | √ | ' ' |  |
| 13 | fdecisonlevelhide | fdecisonlevelhide | int8 | 64 |  | √ | 0 |  |
| 14 | fspecial | fspecial | varchar | 50 |  | √ | ' ' |  |
| 15 | fsumamount | fsumamount | numeric | 23 | 10 | √ | 0 |  |
| 16 | flevelid | flevelid | int8 | 64 |  | √ | 0 |  |
| 17 | fsceneitem | fsceneitem | bpchar | 1 |  | √ | ' ' |  |
| 18 | fsigningcycle | 合同有效期限 | varchar | 50 |  | √ | ' ' | 合同有效期限 |
| 19 | fbillno | 项目立项编号 | varchar | 60 |  | √ | ' ' | 项目立项编号 |
| 20 | fdecisonlevelld | fdecisonlevelld | int8 | 64 |  | √ | 0 |  |
| 21 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :保存 B :已提交 C :已审核 D :已作废 |
| 22 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 23 | fisselloff | fisselloff | varchar | 30 |  | √ | '0' |  |
| 24 | fservicetype | fservicetype | int8 | 64 |  | √ | 0 |  |
| 25 | fdecisiontypeid | fdecisiontypeid | int8 | 64 |  | √ | 0 |  |
| 26 | fproject | fproject | varchar | 50 |  | √ | ' ' |  |
| 27 | fsrcbilltype | fsrcbilltype | varchar | 50 |  | √ | ' ' |  |
| 28 | fisproject2 | 下推类型 | bpchar | 1 |  | √ | '0' | 下推类型,枚举: 0 :按场景下推项目启动 1 :列表手工下推项目启动 2 :审核自动下推项目启动 |
| 29 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 30 | fbusiarea | fbusiarea | int8 | 64 |  | √ | 0 |  |
| 31 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |
| 32 | fdemandaffiliateid | fdemandaffiliateid | int8 | 64 |  | √ | 0 |  |
| 33 | famount | 预估未税金额 | numeric | 23 | 10 | √ | 0 | 预估未税金额 |
| 34 | fpurdeptid | 采购部门 | int8 | 64 |  | √ | 0 | 采购部门 pds_purdepart |
| 35 | fsurplusamount | 预估价税合计 | numeric | 23 | 10 | √ | 0 | 预估价税合计 |
| 36 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 37 | fnotreason | fnotreason | varchar | 100 |  | √ | ' ' |  |
| 38 | fismultiscene | 是否拆分多个寻源场景 | bpchar | 1 |  | √ | '1' | 是否拆分多个寻源场景 |
| 39 | fpurgroupid | 采购组 | int8 | 64 |  | √ | 0 | 采购业务组(封存) bd_pmoperatorgroup |
| 40 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 41 | fpurdecision | 采购决策 | bpchar | 1 |  | √ | ' ' | 采购决策 |
| 42 | ftaxtype | 价格录入方式 | bpchar | 1 |  | √ | '1' | 价格录入方式,枚举: 1 :录入含税价 2 :录入未税价 3 :价内税(含税) |
| 43 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 44 | fk_basedatafield | fk_basedatafield | int8 | 64 |  | √ | 0 |  |
| 45 | fbusitype | fbusitype | varchar | 30 |  | √ | ' ' |  |
| 46 | fchassisttype | fchassisttype | int8 | 64 |  | √ | 0 |  |
| 47 | fparentid | fparentid | varchar | 50 |  | √ | ' ' |  |
| 48 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 49 | fcostattribution | fcostattribution | int8 | 64 |  | √ | 0 |  |
| 50 | fentitykey | fentitykey | varchar | 50 |  | √ | ' ' |  |
| 51 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 52 | fregionid | 所属区域 | int8 | 64 |  | √ | 0 | 区域分组 pds_regiongroup |
| 53 | fisspecial | 特殊采购 | bpchar | 1 |  | √ | '0' | 特殊采购 |
| 54 | fsumqty | fsumqty | numeric | 23 | 10 | √ | 0 |  |
| 55 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 56 | forigncreator | forigncreator | int8 | 64 |  | √ | 0 |  |
| 57 | fpurchasetype | 采购类型 | varchar | 30 |  | √ | ' ' | 采购类型,枚举: 0 :年采 1 :非年采 2 :混和采购 |
| 58 | fsourcetypeid | fsourcetypeid | int8 | 64 |  | √ | 0 |  |
| 59 | fsumtaxamount | fsumtaxamount | numeric | 23 | 10 | √ | 0 |  |
| 60 | fsumtax | fsumtax | numeric | 23 | 10 | √ | 0 |  |
| 61 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_demand |  | fid |
| 2 | idx_src_demand_fbillno |  | fbillno |
| 3 | idx_src_demand_fparentid |  | fparentid |
