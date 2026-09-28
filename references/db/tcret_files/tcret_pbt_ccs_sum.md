# 车船税税源明细-tcret_pbt_ccs_sum

## 单据体-子表 t_tcret_pbt_ccs_sum_entry

- **表名称：** 单据体-子表
- **表名：** t_tcret_pbt_ccs_sum_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fjmamount | 减免税额 | numeric | 23 | 10 | √ | 0 | 减免税额 |
| 3 | fstart | 减免起始时间 | timestamp | 0 |  |  | null | 减免起始时间 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | ftaxdeduction | 减免性质代码 | int8 | 64 |  | √ | 0 | 减免政策代码 tpo_taxdeduction |
| 6 | fend | 减免终止时间 | timestamp | 0 |  |  | null | 减免终止时间 |
| 7 | fjmbl | 减免比例 | numeric | 23 | 10 | √ | 0 | 减免比例 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcret_pbt_ccs_sum_entry_fk |  | fid |
| 2 | pk_tcret_pbt_ccs_sum_entry |  | fentryid |

---

## 车船税税源明细-主表 t_tcret_pbt_ccs_sum

- **表名称：** 车船税税源明细-主表
- **表名：** t_tcret_pbt_ccs_sum

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faccountorg | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fdraftid | 底稿ID | int8 | 64 |  | √ | 0 | 底稿ID |
| 4 | ftaxrate | 税率 | numeric | 23 | 10 | √ | 0 | 税率 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fsourceid | 税源id | int8 | 64 |  | √ | 0 | 税源id |
| 7 | fmaindataid | 主数据ID（废弃） | int8 | 64 |  | √ | 0 | 主数据ID（废弃） |
| 8 | fccsbdm | 车/船识别代码 | varchar | 50 |  | √ | ' ' | 车/船识别代码 |
| 9 | fccpzdm | 车/船牌照代码 | varchar | 50 |  | √ | ' ' | 车/船牌照代码 |
| 10 | fskssqq | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 11 | fpaidtaxes | 已缴税额 | numeric | 23 | 10 | √ | 0 | 已缴税额 |
| 12 | ftaytype | 税源类型 | varchar | 50 |  | √ | ' ' | 税源类型,枚举: ccscl :车辆 ccscb :船舶 |
| 13 | fybtse | 应补（退）税额 | numeric | 23 | 10 | √ | 0 | 应补（退）税额 |
| 14 | fjmse | 减免税额 | numeric | 23 | 10 | √ | 0 | 减免税额 |
| 15 | fskssqz | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 16 | fzxrq | 注销日期 | timestamp | 0 |  |  | null | 注销日期 |
| 17 | ftaxbasis | 计税依据 | numeric | 23 | 10 | √ | 0 | 计税依据 |
| 18 | fsbbid | 申报表ID | int8 | 64 |  | √ | 0 | [纳税申报表基础资料 bdtaxr_nsrxx](../bdtaxr_files/bdtaxr_nsrxx.md) |
| 19 | fcclx | 车/船类型 | varchar | 50 |  | √ | ' ' | 车/船类型,枚举: |
| 20 | fcczcrq | 车/船注册日期 | timestamp | 0 |  |  | null | 车/船注册日期 |
| 21 | fynse | 应纳税额 | numeric | 23 | 10 | √ | 0 | 应纳税额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcret_pbt_ccs_sum |  | fid |
| 2 | idx_tcret_pbt_ccs_sum_1 |  | forgid,fskssqq,fskssqz |
