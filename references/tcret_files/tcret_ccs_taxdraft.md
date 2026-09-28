# 车船税申报底稿-tcret_ccs_taxdraft

## 车船税申报底稿-主表 t_tcret_ccs_taxdraft

- **表名称：** 车船税申报底稿-主表
- **表名：** t_tcret_ccs_taxdraft

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
| 8 | fdeclareid | 申报表id | int8 | 64 |  | √ | 0 | 申报表id |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fcollectiondate | 采集日期 | timestamp | 0 |  |  | null | 采集日期 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fdeclarestatus | 申报表申报状态 | varchar | 50 |  | √ | ' ' | 申报表申报状态,枚举: editing :● 未申报 declaring :● 申报中 declared :● 申报成功 undeclare :● 未编制 declarefailed :● 申报失败 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fdeclarebillstatus | 申报表单据状态 | varchar | 50 |  | √ | ' ' | 申报表单据状态,枚举: A :暂存 B :已提交 C :已审核 D :重新审核 |
| 15 | ftaxoffice | 税务机关 | int8 | 64 |  | √ | 0 | 税务机关 bastax_taxorgan |
| 16 | fbillno | 底稿编号 | varchar | 30 |  | √ | ' ' | 底稿编号 |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fdeclarenumber | 申报表编号 | varchar | 50 |  | √ | ' ' | 申报表编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcret_ccs_taxdraft |  | fid |
| 2 | idx_ccs_taxdraft_forgid |  | forgid,ftaxoffice,fcollectiondate |

---

## 单据体-子表 t_tcret_ccs_taxdraft_en

- **表名称：** 单据体-子表
- **表名：** t_tcret_ccs_taxdraft_en

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxrate | 税率 | numeric | 23 | 10 | √ | 0 | 税率 |
| 3 | fsourceid | 税源id | int8 | 64 |  | √ | 0 | 税源id |
| 4 | fcurrency | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fcurrentpayable | 本期应纳税额 | numeric | 23 | 10 | √ | 0 | 本期应纳税额 |
| 7 | fccsbdm | 车/船识别代码 | varchar | 50 |  | √ | ' ' | 车/船识别代码,枚举: |
| 8 | fccpzdm | 车/船牌照代码 | varchar | 50 |  | √ | ' ' | 车/船牌照代码,枚举: 1 :划拨 2 :出让 3 :转让 4 :租赁 5 :其他 |
| 9 | fskssqq | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 10 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fpaidtaxes | 已缴税额 | numeric | 23 | 10 | √ | 0 | 已缴税额 |
| 12 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fybtse | 应补（退）税额 | numeric | 23 | 10 | √ | 0 | 应补（退）税额 |
| 14 | fskssqz | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 15 | fzxrq | 注销日期 | timestamp | 0 |  |  | null | 注销日期 |
| 16 | ftaxbasis | 计税依据 | numeric | 23 | 10 | √ | 0 | 计税依据 |
| 17 | fcclx | 车/船类型 | varchar | 50 |  | √ | ' ' | 车/船类型,枚举: ccscl :车辆 ccscb :船舶 |
| 18 | fcczcrq | 车/船注册日期 | timestamp | 0 |  |  | null | 车/船注册日期 |
| 19 | fnumber | 资产编号 | varchar | 50 |  | √ | ' ' | 资产编号 |
| 20 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 21 | fcurrentjmamount | 本期减免税额 | numeric | 23 | 10 | √ | 0 | 本期减免税额 |
| 22 | ftaxtype | 税源类型 | varchar | 50 |  | √ | ' ' | 税源类型,枚举: ccscl :车辆 ccscb :船舶 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcret_ccs_taxdraft_en_fk |  | fid |
| 2 | pk_tcret_ccs_taxdraft_en |  | fentryid |
