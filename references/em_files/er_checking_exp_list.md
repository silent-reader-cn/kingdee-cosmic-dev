# 部门费用清单-er_checking_exp_list

## 关联子实体-子表 t_er_checking_exp_detail_lk

- **表名称：** 关联子实体-子表
- **表名：** t_er_checking_exp_detail_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_checking_exp_detail_lk |  | fpkid |

---

## 部门费用清单-关联追踪表 t_er_checking_exp_list_tc

- **表名称：** 部门费用清单-关联追踪表
- **表名：** t_er_checking_exp_list_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  | √ | 0 |  |
| 3 | fttableid | fttableid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | ftid | ftid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_checking_exp_list_tc_tbill |  | ftbillid |
| 2 | pk_t_er_checking_exp_list_tc |  | fid |
| 3 | idx_er_checking_exp_list_tc_tid |  | ftid |

---

## 订单信息-子表 t_er_checking_exp_detail

- **表名称：** 订单信息-子表
- **表名：** t_er_checking_exp_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdepartaddress | 上车地点 | varchar | 255 |  | √ | ' ' | 上车地点 |
| 3 | ftotalamount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 4 | fordernum | 结算单号 | varchar | 50 |  | √ | ' ' | 结算单号 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fcityname | 用车城市 | varchar | 50 |  | √ | ' ' | 用车城市 |
| 7 | fdistance | 公里数 | varchar | 50 |  | √ | ' ' | 公里数 |
| 8 | fvehicletype | 用车类型 | varchar | 100 |  | √ | ' ' | 用车类型 |
| 9 | fsourcebookedid | 预订人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fvendorname | 供应商名称 | varchar | 50 |  | √ | ' ' | 供应商名称 |
| 11 | farriveaddress | 下车地点 | varchar | 255 |  | √ | ' ' | 下车地点 |
| 12 | fhappenddate | 结算发生日期 | timestamp | 0 |  |  | null | 结算发生日期 |
| 13 | fisconfirm | 是否确认 | varchar | 10 |  | √ | ' ' | 是否确认 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 15 | fusetime | 用车时间 | timestamp | 0 |  |  | null | 用车时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_checking_exp_detail |  | fentryid |

---

## 部门费用清单-反写记录表 t_er_checking_exp_list_wb

- **表名称：** 部门费用清单-反写记录表
- **表名：** t_er_checking_exp_list_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foperate | foperate | varchar | 50 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 | √ | 0 |  |
| 8 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_checking_exp_list_wb |  | fentryid |

---

## 部门费用清单-主表 t_er_checking_exp_list

- **表名称：** 部门费用清单-主表
- **表名：** t_er_checking_exp_list

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fconfirmamount | 确认金额 | numeric | 23 | 10 | √ | 0 | 确认金额 |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :审核通过 D :审核未通过 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fcostdeptid | 部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fcurrency | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fmsgcount | 消息通知次数 | int8 | 64 |  | √ | 0 | 消息通知次数 |
| 11 | fneedsend | 是否需要推送 | bpchar | 1 |  | √ | '0' | 是否需要推送 |
| 12 | fcheckingtotalamount | 总金额 | numeric | 23 | 10 | √ | 0 | 总金额 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fperiod | 期间 | timestamp | 0 |  |  | null | 期间 |
| 15 | fcostcompanyid | 公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 16 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fformid | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: er_planecheckingbill :机票 er_hotelcheckingbill :酒店 er_traincheckingbill :火车 er_vehiclecheckingbill :用车 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_checking_exp_list |  | fid |

---

## 关联子实体-子表 t_er_checking_exp_list_lk

- **表名称：** 关联子实体-子表
- **表名：** t_er_checking_exp_list_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_er_checking_exp_list_lk |  | fpkid |
| 2 | idx_er_checking_exp_list_lk_fk |  | fid |

---

## 消息推送人-多选基础资料表 t_er_vehicle_exp_user

- **表名称：** 消息推送人-多选基础资料表
- **表名：** t_er_vehicle_exp_user

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_vehicle_exp_user |  | fpkid |
