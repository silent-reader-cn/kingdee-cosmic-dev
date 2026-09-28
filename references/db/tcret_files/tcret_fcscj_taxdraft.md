# 从价计征房产税申报底稿-tcret_fcscj_taxdraft

## 单据体-子表 t_tcret_fcscj_taxdraft_en

- **表名称：** 单据体-子表
- **表名：** t_tcret_fcscj_taxdraft_en

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fassertvalue | 房产原值 | numeric | 23 | 10 | √ | 0 | 房产原值 |
| 3 | ftaxratio | 计税比例 | numeric | 23 | 10 | √ | 0 | 计税比例 |
| 4 | ftaxrate | 税率 | numeric | 23 | 10 | √ | 0 | 税率 |
| 5 | fsourceid | 房产编号 | int8 | 64 |  | √ | 0 | 房产基础信息 tdm_fcs_basic_info |
| 6 | fcurrency | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fcurrentpayable | 本期应纳税额 | numeric | 23 | 10 | √ | 0 | 本期应纳税额 |
| 9 | fskssqq | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 10 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fpaidtaxes | 已缴税额 | numeric | 23 | 10 | √ | 0 | 已缴税额 |
| 12 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fybtse | 应补（退）税额 | numeric | 23 | 10 | √ | 0 | 应补（退）税额 |
| 14 | fskssqz | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 15 | ftaxbasis | 计税依据 | numeric | 23 | 10 | √ | 0 | 计税依据 |
| 16 | frentalvalue | 出租房产原值 | numeric | 23 | 10 | √ | 0 | 出租房产原值 |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 18 | fcurrentjmamount | 本期减免税额 | numeric | 23 | 10 | √ | 0 | 本期减免税额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcret_fcscj_taxdraft_en |  | fentryid |
| 2 | idx_tcret_fcscj_taxdraft_en_fk |  | fid |

---

## 从价计征房产税申报底稿-主表 t_tcret_fcscj_taxdraft

- **表名称：** 从价计征房产税申报底稿-主表
- **表名：** t_tcret_fcscj_taxdraft

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faccountorg | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fsumybtse | 合计应补（退）税额 | numeric | 23 | 10 | √ | 0 | 合计应补（退）税额 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fisxxwlqy | 小型微利企业 | varchar | 50 |  | √ | ' ' | 小型微利企业,枚举: 1 :是 0 :否 |
| 9 | fdeclareid | 申报表id | int8 | 64 |  | √ | 0 | 申报表id |
| 10 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 11 | fcollectiondate | 采集日期 | timestamp | 0 |  |  | null | 采集日期 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fdeclarestatus | 申报表申报状态 | varchar | 50 |  | √ | ' ' | 申报表申报状态,枚举: editing :● 未申报 declaring :● 申报中 declared :● 申报成功 undeclare :● 未编制 declarefailed :● 申报失败 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fdeclarebillstatus | 申报表单据状态 | varchar | 50 |  | √ | ' ' | 申报表单据状态,枚举: A :暂存 B :已提交 C :已审核 D :重新审核 |
| 16 | ftaxoffice | 税务机关 | int8 | 64 |  | √ | 0 | 税务机关 bastax_taxorgan |
| 17 | fbillno | 底稿编号 | varchar | 30 |  | √ | ' ' | 底稿编号 |
| 18 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fdeclarenumber | 申报表编号 | varchar | 50 |  | √ | ' ' | 申报表编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcret_fcscj_taxdraft |  | fid |
| 2 | idx_fcscj_taxdraft_forgid |  | forgid,ftaxoffice,fcollectiondate |
