# 土地增值税尾盘收入成本台账-tcret_tdzzs_wp_account

## 特定业态计税明细-子表 t_tcret_tdzzs_wp_acc_td

- **表名称：** 特定业态计税明细-子表
- **表名：** t_tcret_tdzzs_wp_acc_td

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodifierfield1 | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fswyt | 税务业态 | varchar | 50 |  | √ | ' ' | 税务业态,枚举: normal_house :普通住宅 un_normal_house :非普通住宅 un_house :其他类型房地产 un_calc_state :非清算业态 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fxsyt | 销售业态 | int8 | 64 |  | √ | 0 | [销售业态 bastax_saleformat](../bastax_files/bastax_saleformat.md) |
| 6 | fmodifydatefield1 | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fqyje | 签约金额（不含税） | numeric | 23 | 10 | √ | 0 | 签约金额（不含税） |
| 8 | fyjsj | 应缴税金 | numeric | 23 | 10 | √ | 0 | 应缴税金 |
| 9 | froombasedata | 房间编码 | int8 | 64 |  | √ | 0 | [房间基础信息 bastax_room](../bastax_files/bastax_room.md) |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fxmqssfl | 项目清算税负率 | numeric | 23 | 10 | √ | 0 | 项目清算税负率 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcret_tdzzs_wp_acc_td |  | fentryid |
| 2 | idx_tcret_tdzzs_wp_acc_td |  | fid |

---

## 尾盘收入成本明细-子表 t_tcret_tdzzs_wp_acc_mx

- **表名称：** 尾盘收入成本明细-子表
- **表名：** t_tcret_tdzzs_wp_acc_mx

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fscmj | 实测面积（平方米） | numeric | 23 | 10 | √ | 0 | 实测面积（平方米） |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fxsyt | 销售业态 | int8 | 64 |  | √ | 0 | [销售业态 bastax_saleformat](../bastax_files/bastax_saleformat.md) |
| 5 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fdwcb | 单位成本 | numeric | 23 | 10 | √ | 0 | 单位成本 |
| 8 | fdwcbsjly | 单位成本数据来源 | varchar | 50 |  | √ | ' ' | 单位成本数据来源,枚举: taxsource :清算税源 manual :手工录入 |
| 9 | fswyt | 税务业态 | varchar | 50 |  | √ | ' ' | 税务业态,枚举: normal_house :普通住宅 un_normal_house :非普通住宅 un_house :其他类型房地产 un_calc_state :非清算业态 |
| 10 | fqyje | 签约金额（不含税） | numeric | 23 | 10 | √ | 0 | 签约金额（不含税） |
| 11 | froombasedata | 房间编码 | int8 | 64 |  | √ | 0 | [房间基础信息 bastax_room](../bastax_files/bastax_room.md) |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fcsjwzcb | 除税金外总成本 | numeric | 23 | 10 | √ | 0 | 除税金外总成本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcret_tdzzs_wp_acc_mx |  | fid |
| 2 | pk_tcret_tdzzs_wp_acc_mx |  | fentryid |

---

## 土地增值税尾盘收入成本台账-主表 t_tcret_tdzzs_wp_acc

- **表名称：** 土地增值税尾盘收入成本台账-主表
- **表名：** t_tcret_tdzzs_wp_acc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | ftdzzsproject | 土地增值税项目 | int8 | 64 |  | √ | 0 | [土地增值税项目 tdm_tdzzs_clearing_unit](../tdm_files/tdm_tdzzs_clearing_unit.md) |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | ftdytqyjehj | 特定业态签约金额合计（不含税） | numeric | 23 | 10 | √ | 0 | 特定业态签约金额合计（不含税） |
| 8 | fmxqyjehj | 签约金额合计（不含税） | numeric | 23 | 10 | √ | 0 | 签约金额合计（不含税） |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fistax | 特定业态是否计税 | bpchar | 1 |  | √ | '0' | 特定业态是否计税 |
| 12 | fenddate | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | ftdytyjsjhj | 特定业态应缴税金合计 | numeric | 23 | 10 | √ | 0 | 特定业态应缴税金合计 |
| 15 | fmxscmjhj | 实测面积合计 | numeric | 23 | 10 | √ | 0 | 实测面积合计 |
| 16 | fmxcsjwzcbhj | 除税金外总成本合计 | numeric | 23 | 10 | √ | 0 | 除税金外总成本合计 |
| 17 | fstartdate | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 18 | fbillno | 台账编号 | varchar | 30 |  | √ | ' ' | 台账编号 |
| 19 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcret_tdzzs_wp_acc |  | fid |
| 2 | idx_tcret_tdzzs_wp_acc |  | forgid,ftdzzsproject,fstartdate,fenddate |

---

## 尾盘收入成本汇总-子表 t_tcret_tdzzs_wp_acc_hz

- **表名称：** 尾盘收入成本汇总-子表
- **表名：** t_tcret_tdzzs_wp_acc_hz

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fwpjsdwcb | 尾盘计税单位成本 | numeric | 23 | 10 | √ | 0 | 尾盘计税单位成本 |
| 3 | fswyt | 税务业态 | varchar | 50 |  | √ | ' ' | 税务业态,枚举: normal_house :普通住宅 un_normal_house :非普通住宅 un_house :其他类型房地产 un_calc_state :非清算业态 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fscmjhj | 实测面积合计（平方米） | numeric | 23 | 10 | √ | 0 | 实测面积合计（平方米） |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fqyjehjbhs | 签约金额合计（不含税） | numeric | 23 | 10 | √ | 0 | 签约金额合计（不含税） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcret_tdzzs_wp_acc_hz |  | fid |
| 2 | pk_tcret_tdzzs_wp_acc_hz |  | fentryid |
