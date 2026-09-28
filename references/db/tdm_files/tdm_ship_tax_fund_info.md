# 船舶税源信息-tdm_ship_tax_fund_info

## 减免登记台账-子表 t_tdm_ship_tax_fund_entry

- **表名称：** 减免登记台账-子表
- **表名：** t_tdm_ship_tax_fund_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fstart | 减免起始时间 | timestamp | 0 |  |  | null | 减免起始时间 |
| 3 | fratio | 减免比例 | numeric | 23 | 10 | √ | 0.0000000000 | 减免比例 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | ftaxdeduction | 减免项目名称及代码 | int8 | 64 |  | √ | 0 | 减免政策代码 tpo_taxdeduction |
| 6 | fend | 减税终止时间 | timestamp | 0 |  |  | null | 减税终止时间 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tdm_ship_tax_fund_entry_fk |  | fid |
| 2 | pk_tdm_ship_tax_fund_entry |  | fentryid |

---

## 船舶税源信息-主表 t_tdm_ship_tax_fund_info

- **表名称：** 船舶税源信息-主表
- **表名：** t_tdm_ship_tax_fund_info

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faccountorg | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | forgfield | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fdwse | 单位税额 | numeric | 23 | 10 | √ | 0 | 单位税额 |
| 5 | fsourcesystem | 来源系统 | varchar | 50 |  | √ | ' ' | 来源系统 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fhomeport | 船籍港 | varchar | 50 |  | √ | ' ' | 船籍港 |
| 8 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fsbyf | 申报月份 | varchar | 50 |  | √ | '12' | 申报月份,枚举: 1 :1月 2 :2月 3 :3月 4 :4月 5 :5月 6 :6月 7 :7月 8 :8月 9 :9月 10 :10月 11 :11月 12 :12月 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fbizdimensiontype | 业务维度 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 13 | fownershipdate | 取得所有权日期 | timestamp | 0 |  |  | null | 取得所有权日期 |
| 14 | fwithheld | 是否代扣代缴 | bpchar | 1 |  | √ | ' ' | 是否代扣代缴 |
| 15 | fshiptype | 船舶种类 | varchar | 50 |  | √ | ' ' | 船舶种类 |
| 16 | fhosttype | 主机种类 | varchar | 50 |  | √ | ' ' | 主机种类 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | ftaxauthority | 主管税务机关 | int8 | 64 |  | √ | 0 | 税务机关 bastax_taxorgan |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fbizdimensionname | 业务维度值 | varchar | 200 |  | √ | ' ' | 业务维度值 |
| 21 | fdatefield | 终止日期 | timestamp | 0 |  |  | null | 终止日期 |
| 22 | fshipnumber | 船舶识别号 | varchar | 50 |  | √ | ' ' | 船舶识别号 |
| 23 | fhulllength | 艇身长度 | numeric | 23 | 10 | √ | 0.0000000000 | 艇身长度 |
| 24 | finitregnumber | 初次登记号码 | varchar | 50 |  | √ | ' ' | 初次登记号码 |
| 25 | fitemcollection | 船舶类型 | varchar | 30 |  | √ | ' ' | 船舶类型,枚举: 1 :净吨位不超过200吨的机动船舶 2 :净吨位超过200吨但不超过2000吨的机动船舶 3 :净吨位超过2000吨但不超过10000吨的机动船舶 4 :净吨位超过10000吨的机动船舶 9 :净吨位不超过200吨的拖船、非机动驳船 10 :净吨位超过200吨但不超过2000吨的拖船、非机动驳船 11 :净吨位超过2000吨但不超过10000吨的拖船、非机动驳船 12 :净吨位超过10000吨的拖船、非机动驳船 5 :艇身长度不超过10米的游艇 6 :艇身长度超过10米但不超过18米的游艇 7 :艇身长度超过18米但不超过30米的游艇 8 :艇身长度超过30米的游艇 13 :辅助动力帆艇 |
| 26 | fjdw | 净吨位 | numeric | 23 | 10 | √ | 0 | 净吨位 |
| 27 | fenable | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: 0 :禁用 1 :可用 |
| 28 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源 |
| 29 | fnettonnage | 净吨位-小数废弃 | int8 | 64 |  | √ | 0 | 净吨位-小数废弃 |
| 30 | fnumber | 资产编号 | varchar | 30 |  | √ | ' ' | 资产编号 |
| 31 | fcompletiondate | 建成日期 | timestamp | 0 |  |  | null | 建成日期 |
| 32 | fbizdimensionid | 业务维度值ID | varchar | 50 |  | √ | ' ' | 业务维度值ID |
| 33 | fmainpower | 主机功率 | int8 | 64 |  | √ | 0 | 主机功率 |
| 34 | fofficialnumber | 船舶登记号 | varchar | 50 |  | √ | ' ' | 船舶登记号 |
| 35 | fdateissue | 发证日期 | timestamp | 0 |  |  | null | 发证日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tdm_ship_tax_fund_info_pkey |  | fid |
| 2 | idx_tdm_ship_tax_fund_info |  | fnumber |

---

## 船舶税源信息-多语言表 t_tdm_ship_tax_fund_info_l

- **表名称：** 船舶税源信息-多语言表
- **表名：** t_tdm_ship_tax_fund_info_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 中文船名 | varchar | 100 |  | √ | ' ' | 中文船名 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tdm_ship_tax_fund_info_l_0 |  | fid,flocaleid |
| 2 | t_tdm_ship_tax_fund_info_l_pkey |  | fpkid |
