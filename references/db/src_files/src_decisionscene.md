# 采委会寻源场景F7(删除)-src_decisionscene

## 供应商信息-子表 t_src_decisionsup

- **表名称：** 供应商信息-子表
- **表名：** t_src_decisionsup

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsuppliertype | fsuppliertype | varchar | 30 |  | √ | ' ' |  |
| 3 | fsupplier | 供应商 | int8 | 64 |  | √ | 0 | [注册供应商 src_supplier](../pds_files/src_supplier.md) |
| 4 | fentryidtwo | fentryidtwo | int8 | 64 |  | √ | 0 |  |
| 5 | fisinvite | 是否邀请 | bpchar | 1 |  | √ | '0' | 是否邀请 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | freason | 备注 | varchar | 100 |  | √ | ' ' | 备注 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fsource | 来源 | varchar | 30 |  | √ | ' ' | 来源,枚举: 1 :来源采委会 2 :立项新增 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryidtwo | fentryidtwo |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_decisionsup |  | fentryidtwo |
| 2 | idx_src_decisionsup_fid |  | fid |

---

## 采购组织-多选基础资料表 t_src_decisionsceneorg

- **表名称：** 采购组织-多选基础资料表
- **表名：** t_src_decisionsceneorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_decisceneorg_eid |  | fentryid |
| 2 | pk_src_decisionsceneorg |  | fpkid |
| 3 | idx_src_decisceneorg_bid |  | fbasedataid |

---

## 品类-多选基础资料表 t_src_categorydecision

- **表名称：** 品类-多选基础资料表
- **表名：** t_src_categorydecision

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [物料分类 bd_materialgroup](../basedata_files/bd_materialgroup.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_categorydecision_fid |  | fentryid |
| 2 | idx_src_categorydecision_bid |  | fbasedataid |
| 3 | pk_src_categorydecision |  | fpkid |

---

## 采委会寻源场景F7(删除)-主表 t_src_decisionscene

- **表名称：** 采委会寻源场景F7(删除)-主表
- **表名：** t_src_decisionscene

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 2 | fotherruleassess | fotherruleassess | varchar | 1000 |  | √ | ' ' |  |
| 3 | fsceneno_des | fsceneno_des | varchar | 100 |  | √ | ' ' |  |
| 4 | fsceneamount | fsceneamount | numeric | 23 | 10 | √ | 0 |  |
| 5 | fotherreason | 其他独家谈判原因 | varchar | 255 |  | √ | ' ' | 其他独家谈判原因 |
| 6 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 7 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 8 | fbargainrule | fbargainrule | varchar | 30 |  | √ | ' ' |  |
| 9 | fsuppliernum | fsuppliernum | int8 | 64 |  | √ | 0 |  |
| 10 | ftitle | 采委会名称 | varchar | 50 |  | √ | ' ' | 采委会名称 |
| 11 | frange | 场景金额适用范围 | varchar | 50 |  | √ | ' ' | 场景金额适用范围 |
| 12 | fscenestatus | fscenestatus | bpchar | 1 |  | √ | ' ' |  |
| 13 | fchassisttypeid | 底盘类型 | int8 | 64 |  | √ | 0 | [招标辅助资料 pds_extdata](../pds_files/pds_extdata.md) |
| 14 | fprojectno | fprojectno | varchar | 50 |  | √ | ' ' |  |
| 15 | fdetailid | fdetailid | varchar | 50 |  | √ | ' ' |  |
| 16 | fbillno | 场景编码 | varchar | 100 |  | √ | ' ' | 场景编码 |
| 17 | fwinrule | 中标原则 | int8 | 64 |  | √ | 0 | [招标辅助资料 pds_extdata](../pds_files/pds_extdata.md) |
| 18 | fisfunction | 生效状态 | bpchar | 1 |  | √ | '0' | 生效状态,枚举: A :未生效 B :生效 C :失效 D :过期 |
| 19 | fprojectid | fprojectid | int8 | 64 |  | √ | 0 |  |
| 20 | fbillstatus | fbillstatus | bpchar | 1 |  | √ | ' ' |  |
| 21 | fbillno2 | 采委会单号 | varchar | 50 |  | √ | ' ' | 采委会单号 |
| 22 | fwinerqty | 中标供应商数量 | int8 | 64 |  | √ | 0 | 中标供应商数量 |
| 23 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 24 | fscenename_des | 场景名称 | varchar | 100 |  | √ | ' ' | 场景名称 |
| 25 | fpurtype | 寻源方式 | int8 | 64 |  | √ | 0 | [招标辅助资料 pds_extdata](../pds_files/pds_extdata.md) |
| 26 | fruleassess | 商务报价计算规则（评估） | varchar | 30 |  | √ | ' ' | 商务报价计算规则（评估）,枚举: 1 :标的单价 2 :报价包的采购总金额 3 :报价包内所有产品的平均价 4 :其他 |
| 27 | fquerycondition | 邀请条件 | varchar | 255 |  | √ | ' ' | 邀请条件 |
| 28 | fscenechasisstid | fscenechasisstid | int8 | 64 |  | √ | 0 |  |
| 29 | fentryid | 主键 | int8 | 64 |  | √ | 0 | 主键 |
| 30 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 31 | fotherwinrule | 其他中标原则 | varchar | 1000 |  | √ | ' ' | 其他中标原则 |
| 32 | fbizstatus | 确认状态 | bpchar | 1 |  | √ | ' ' | 确认状态,枚举: A :待确认 B :通过 C :未通过 |
| 33 | famount | 场景金额 | numeric | 23 | 10 | √ | 0 | 场景金额 |
| 34 | fseq1 | 寻源场景编号 | varchar | 50 |  | √ | ' ' | 寻源场景编号 |
| 35 | fcompreper | 商务综合占比(%) | numeric | 23 | 10 | √ | 0 | 商务综合占比(%) |
| 36 | fwinrule2 | fwinrule2 | int8 | 64 |  | √ | 0 |  |
| 37 | fstatus | 启用状态 | bpchar | 1 |  | √ | ' ' | 启用状态 |
| 38 | fbiztype | fbiztype | varchar | 30 |  | √ | ' ' |  |
| 39 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 40 | faftertalkrule | 标后谈判原则 | varchar | 1000 |  | √ | ' ' | 标后谈判原则 |
| 41 | fsolereason | 独家谈判原因 | varchar | 100 |  | √ | ' ' | 独家谈判原因 |
| 42 | forderrule | 订单分配规则 | varchar | 1000 |  | √ | ' ' | 订单分配规则 |
| 43 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 44 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 45 | ftalkrule | 谈判原则 | int8 | 64 |  | √ | 0 | [招标辅助资料 pds_extdata](../pds_files/pds_extdata.md) |
| 46 | fskillper | 技术标占比(%) | numeric | 23 | 10 | √ | 0 | 技术标占比(%) |
| 47 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 48 | forigncreator | forigncreator | int8 | 64 |  | √ | 0 |  |
| 49 | fbusinessper | 商务标占比(%) | numeric | 23 | 10 | √ | 0 | 商务标占比(%) |
| 50 | fisprice | fisprice | bpchar | 1 |  | √ | '0' |  |
| 51 | fsrcflowconfig | fsrcflowconfig | int8 | 64 |  | √ | 0 |  |
| 52 | fdiscardrule | 废标原则 | varchar | 1000 |  | √ | ' ' | 废标原则 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_deciscene_pid |  | fprojectid |
| 2 | pk_src_decisionscene |  | fentryid |
| 3 | idx_src_deciscene_fid |  | fid |
