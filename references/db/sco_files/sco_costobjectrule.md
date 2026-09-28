# 成本核算对象规则-sco_costobjectrule

## 成本核算对象规则-主表 t_sco_costobjectrule

- **表名称：** 成本核算对象规则-主表
- **表名：** t_sco_costobjectrule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpnoruleass | 生产编号前缀 | varchar | 80 |  | √ | ' ' | 生产编号前缀 |
| 3 | fcostcalcdimensionid | 成本核算维度 | int8 | 64 |  | √ | 0 | [成本核算维度 sco_costcalcdimension](../sco_files/sco_costcalcdimension.md) |
| 4 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fbiztype | 成本计算方法 | varchar | 30 |  | √ | ' ' | 成本计算方法,枚举: RO :工单成本 SO :分批法 PZ :品种法 FL :分类法 SW :服务工单 SP :服务项目 RE :重复制造 CU :自定义 |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 9 | fobjrule | 默认编码规则 | varchar | 30 |  | √ | ' ' | 默认编码规则,枚举: CR_SRC :成本中心编码-源单编码-源单行号 CR_PRO :成本中心编码-产品编码-生产编号 CR_CP :成本中心编码-产品编码 CR_CEN :成本中心编码 CR_COP :成本中心编码-项目号 |
| 10 | frulenameext | 名称可配置项 | varchar | 255 |  | √ | ' ' | 名称可配置项,枚举: |
| 11 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 13 | fobjruleass | 编码规则前缀 | varchar | 80 |  | √ | ' ' | 编码规则前缀 |
| 14 | frulenumberext | 编码可配置项 | varchar | 255 |  | √ | ' ' | 编码可配置项,枚举: |
| 15 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 16 | fobjrulename | 默认名称规则 | varchar | 255 |  | √ | ' ' | 默认名称规则,枚举: CRN_SRC :成本中心名称-源单编码-源单行号 CRN_PRO :成本中心名称-产品名称-生产编号 CRN_CP :成本中心名称-产品名称 CRN_COP :成本中心名称-项目号 |
| 17 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 18 | frule | 核算规则 | varchar | 30 |  | √ | ' ' | 核算规则,枚举: SN :源单单号+源单行号 PN :产品+生产编号 CP :产品 RULE_SW :源单单号+源单行号+项目号 RULE_SP :项目号 CU :自定义 RE :生产线+产品+物料版本+辅助属性 |
| 19 | fobgrulenameass | 名称规则前缀 | varchar | 80 |  | √ | ' ' | 名称规则前缀 |
| 20 | fsotype | 源单类型 | varchar | 30 |  | √ | ' ' | 源单类型,枚举: PB :工单/委外工单 SB :生产编号 SOTYPE_SW :检修工单 SOTYPE_SP :项目 |
| 21 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 22 | faccountorgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 23 | fnumber | 编码 | varchar | 255 |  | √ | ' ' | 编码 |
| 24 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 25 | fpnorule | 生产编号规则 | varchar | 30 |  | √ | ' ' | 生产编号规则,枚举: 000001 :流水号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_sco_costobjectrule |  | fmasterid,faccountorgid,fcostcenterid |
| 2 | pk_sco_costobjectrule |  | fid |

---

## 成本核算对象规则-多语言表 t_sco_costobjectrule_l

- **表名称：** 成本核算对象规则-多语言表
- **表名：** t_sco_costobjectrule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 510 |  | √ | ' ' | 备注 |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_sco_costobjectrule_l |  | fid,flocaleid |
| 2 | pk_sco_costobjectrule_l |  | fpkid |
