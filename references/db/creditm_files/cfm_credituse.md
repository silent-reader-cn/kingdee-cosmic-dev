# 授信额度占用单-cfm_credituse

## 授信额度占用单-主表 t_cfm_credituse

- **表名称：** 授信额度占用单-主表
- **表名：** t_cfm_credituse

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcredittypeid | 授信类别 | int8 | 64 |  | √ | 0 | [授信类别 cfm_credittype](../creditm_files/cfm_credittype.md) |
| 3 | forgid | 使用单位 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | famount | 已使用额度 | numeric | 19 | 6 | √ | 0.000000 | 已使用额度 |
| 5 | fcreditprop | fcreditprop | varchar | 50 |  | √ | ' ' |  |
| 6 | fcreditvariety | 授信业务品种 | varchar | 255 |  | √ | ' ' | 授信业务品种 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 9 | fenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fbizcreditamount | 业务占用授信金额 | numeric | 23 | 10 | √ | 0 | 业务占用授信金额 |
| 12 | fsourcetype | 单据类型 | varchar | 50 |  | √ | ' ' | 单据类型 |
| 13 | fctrltype | 控制方式 | varchar | 50 |  | √ | ' ' | 控制方式,枚举: exclusive :专用 share :共享 |
| 14 | fpreamount | 预占额度 | numeric | 23 | 10 | √ | 0 | 预占额度 |
| 15 | fsourcebillno | 源单编号 | varchar | 80 |  | √ | ' ' | 源单编号 |
| 16 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 17 | favaramt | 可用额度 | numeric | 19 | 6 | √ | 0.000000 | 可用额度 |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fsourcebillentryid | 分录id | int8 | 64 |  | √ | 0 | 分录id |
| 20 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | frealamt | 实际占用额度 | numeric | 19 | 6 | √ | 0.000000 | 实际占用额度 |
| 23 | fsourcename | 单据名称 | varchar | 50 |  | √ | ' ' | 单据名称 |
| 24 | foperatetime | foperatetime | timestamp | 0 |  |  | null |  |
| 25 | fbizcurrencyid | 业务币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 26 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 27 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 28 | fiscopy | 是否为续授信拷贝单 | bpchar | 1 |  | √ | '0' | 是否为续授信拷贝单 |
| 29 | ftotalamt | 总授信额度 | numeric | 19 | 6 | √ | 0.000000 | 总授信额度 |
| 30 | freturnamt | 已返还额度 | numeric | 19 | 6 | √ | 0.000000 | 已返还额度 |
| 31 | fstartdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 32 | fcreditrate | 折授信币别汇率 | numeric | 23 | 10 | √ | 0 | 折授信币别汇率 |
| 33 | fbizdate | fbizdate | timestamp | 0 |  |  | null |  |
| 34 | fsourcebillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 35 | fcreditratio | 占用授信比例 | numeric | 23 | 10 | √ | 0 | 占用授信比例 |
| 36 | fcurrencyid | 额度币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 37 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 38 | fcreditlimitid | 授信额度占用单 | int8 | 64 |  | √ | 0 | [授信合同 cfm_creditlimit](../creditm_files/cfm_creditlimit.md) |
| 39 | flocamt | 金额折本位币 | numeric | 19 | 6 | √ | 0.000000 | 金额折本位币 |
| 40 | fcompanyid | fcompanyid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cfm_credituse_status |  | fbillstatus,fcreditlimitid |
| 2 | t_cfm_credituse_pkey |  | fid |
| 3 | idx_cfm_credituse_sid |  | fsourcebillid,fsourcetype,fsourcebillentryid |
| 4 | idx_cfm_credituse_no |  | fbillno |

---

## 授信额度占用单-多语言表 t_cfm_credituse_l

- **表名称：** 授信额度占用单-多语言表
- **表名：** t_cfm_credituse_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 50 |  | √ | ' ' | localeid |
| 3 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 4 | fpkid | fpkid | varchar | 80 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cfm_credituse_l_pkey |  | fpkid |
| 2 | idx_cfm_credituse_l_id |  | fid,flocaleid |

---

## 单据体-子表 t_cfm_credituse_return

- **表名称：** 单据体-子表
- **表名：** t_cfm_credituse_return

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbizbillid | 业务单据ID | int8 | 64 |  | √ | 0 | 业务单据ID |
| 3 | freturntime | 业务时间 | timestamp | 0 |  |  | null | 业务时间 |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | freturnid | 返还ID | int8 | 64 |  | √ | 0 | 返还ID |
| 6 | fbizamount | 业务返还金额 | numeric | 23 | 10 | √ | 0 | 业务返还金额 |
| 7 | foperatetime | 执行时间 | timestamp | 0 |  |  | null | 执行时间 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | famount | 实际返还金额 | numeric | 23 | 10 | √ | 0 | 实际返还金额 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fbilltype | 单据类型 | varchar | 50 |  | √ | ' ' | 单据类型 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cfm_credituse_return_id |  | fid |
| 2 | pk_t_cfm_credituse_return |  | fentryid |
| 3 | idx_cfm_return_uniqueid |  | freturnid |
