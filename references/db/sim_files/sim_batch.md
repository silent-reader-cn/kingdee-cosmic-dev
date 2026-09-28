# 待开发票(旧)-sim_batch

## 明细单据体-子表 t_sim_batch_item

- **表名称：** 明细单据体-子表
- **表名：** t_sim_batch_item

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsimplegoodsname | 分类编码简称 | varchar | 50 |  | √ | ' ' | 分类编码简称 |
| 3 | ftaxrate | 税率 | varchar | 30 |  | √ | ' ' | 税率,枚举: 0.00 :0 0.01 :1% 0.03 :3% 0.05 :5% 0.06 :6% 0.09 :9% 0.10 :10% 0.11 :11% 0.13 :13% 0.15 :15% 0.16 :16% 0.17 :17% |
| 4 | fdiscountrate | 折扣率 | numeric | 23 | 10 | √ | 0.0000000000 | 折扣率 |
| 5 | frowtype | 发票行性质 | varchar | 30 |  | √ | ' ' | 发票行性质,枚举: 0 :明细行 1 :折扣行 2 :被折扣行 |
| 6 | fpolicycontants | 优惠政策内容 | varchar | 50 |  | √ | ' ' | 优惠政策内容 |
| 7 | fdiscountamount | 折扣金额 | numeric | 23 | 10 | √ | 0.0000000000 | 折扣金额 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 10 | fnum | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 11 | funitprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 12 | fgoodsname | 商品名称 | varchar | 160 |  | √ | ' ' | 商品名称 |
| 13 | fspecification | 规格型号 | varchar | 50 |  | √ | ' ' | 规格型号 |
| 14 | fbillsourceid | 单据来源id | varchar | 50 |  | √ | ' ' | 单据来源id |
| 15 | fzzstsgl | 增值税特殊管理 | varchar | 50 |  | √ | ' ' | 增值税特殊管理 |
| 16 | fspbm | 商品编码 | varchar | 50 |  | √ | ' ' | 商品编码 |
| 17 | ftaxamount | 含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 含税金额 |
| 18 | fpolicylogo | 优惠政策标识 | varchar | 30 |  | √ | ' ' | 优惠政策标识,枚举: 0 :未使用 1 :已使用 |
| 19 | ftaxflag | 含税标识 | varchar | 50 |  | √ | ' ' | 含税标识 |
| 20 | fzerotaxmark | 零税率标识 | varchar | 50 |  | √ | ' ' | 零税率标识 |
| 21 | ftaxpremark | 税收优惠政策标识 | varchar | 50 |  | √ | ' ' | 税收优惠政策标识 |
| 22 | ftaxunitprice | 含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 含税单价 |
| 23 | fgoodscode | 税收分类编码 | varchar | 50 |  | √ | ' ' | 税收分类编码 |
| 24 | ftax | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 25 | fzxbm | 纳税人自行编码 | varchar | 50 |  | √ | ' ' | 纳税人自行编码 |
| 26 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 27 | funit | 单位 | varchar | 50 |  | √ | ' ' | 单位 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sim_batch_item_fk |  | fid |
| 2 | pk_sim_batch_item |  | fentryid |

---

## 待开发票(旧)-主表 t_sim_batch

- **表名称：** 待开发票(旧)-主表
- **表名：** t_sim_batch

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbuyeraddr | 购方地址电话 | varchar | 180 |  | √ | ' ' | 购方地址电话 |
| 3 | fdrawer | 开票人 | varchar | 50 |  | √ | ' ' | 开票人 |
| 4 | fmainreason | 开票失败原因 | varchar | 1500 |  | √ | ' ' | 开票失败原因 |
| 5 | fbatchstate | 开票状态 | varchar | 30 |  | √ | ' ' | 开票状态,枚举: 0 :开票成功 1 :开票中 2 :未开票 3 :开票失败 4 :已作废 5 :已红冲 |
| 6 | fpayee | 收款人 | varchar | 50 |  | √ | ' ' | 收款人 |
| 7 | ftotalamount | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 8 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fhsbz | 是否含税 | varchar | 30 |  | √ | ' ' | 是否含税,枚举: 0 :不含税 1 :含税 |
| 10 | ftaxedtype | 征税方式 | varchar | 30 |  | √ | ' ' | 征税方式,枚举: 0 :普通征税 2 :差额征税 |
| 11 | fbilldate | 单据日期 | timestamp | 0 |  |  | null | 单据日期 |
| 12 | fbillstate | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: 0 :正常 1 :异常 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fbatchbelong | 所属批次 | varchar | 50 |  | √ | ' ' | 所属批次 |
| 15 | ftotaltax | 合计税额 | numeric | 23 | 10 | √ | 0.0000000000 | 合计税额 |
| 16 | fissuetime | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 17 | fsaleraddr | 销方地址电话 | varchar | 180 |  | √ | ' ' | 销方地址电话 |
| 18 | finvoicecode | 发票代码 | varchar | 50 |  | √ | ' ' | 发票代码 |
| 19 | freviewer | 复核人 | varchar | 50 |  | √ | ' ' | 复核人 |
| 20 | fspecialtype | 特殊票种 | varchar | 30 |  | √ | ' ' | 特殊票种,枚举: 00 :非特殊票种 02 :收购 06 :抵扣通行费 07 :不抵扣通行费 08 :成品油 |
| 21 | fbuyername | 购方名称 | varchar | 150 |  | √ | ' ' | 购方名称 |
| 22 | finvoiceno | 发票号码 | varchar | 50 |  | √ | ' ' | 发票号码 |
| 23 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 24 | fsalertaxno | 销方纳税人识别号 | varchar | 50 |  | √ | ' ' | 销方纳税人识别号 |
| 25 | fbuyertaxno | 购方纳税人识别号 | varchar | 50 |  | √ | ' ' | 购方纳税人识别号 |
| 26 | fsalerbank | 销方开户行及账号 | varchar | 180 |  | √ | ' ' | 销方开户行及账号 |
| 27 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 28 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 29 | fcopyflag | 复制标记 | int8 | 64 |  | √ | 0 | 复制标记 |
| 30 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 31 | fbuyerphone | 购方手机号 | varchar | 50 |  | √ | ' ' | 购方手机号 |
| 32 | fdeduction | 扣除额 | numeric | 23 | 10 | √ | 0.0000000000 | 扣除额 |
| 33 | forderno | 发票流水号 | varchar | 50 |  | √ | ' ' | 发票流水号 |
| 34 | fissuesource | 开票来源 | varchar | 30 |  | √ | ' ' | 开票来源,枚举: 0 :税务ukey 1 :税控盘 2 :金税盘 3 :税控虚拟ukey |
| 35 | fbuyerproperty | 购方企业类型 | varchar | 30 |  | √ | ' ' | 购方企业类型,枚举: 0 :企业 1 :个人 |
| 36 | finvoicetype | 发票种类 | varchar | 30 |  | √ | ' ' | 发票种类,枚举: 026 :电子普通发票 028 :电子专用发票 007 :纸质普通发票 004 :纸质专用发票 |
| 37 | fbuyerbank | 购方开户行及账号 | varchar | 180 |  | √ | ' ' | 购方开户行及账号 |
| 38 | finvoiceamount | 合计金额 | numeric | 23 | 10 | √ | 0.0000000000 | 合计金额 |
| 39 | fsalername | 销方名称 | varchar | 150 |  | √ | ' ' | 销方名称 |
| 40 | fissuetype | 开票方式 | varchar | 30 |  | √ | ' ' | 开票方式,枚举: 0 :蓝票 1 :红票 |
| 41 | fsystemsource | 数据系统来源 | varchar | 50 |  | √ | ' ' | 数据系统来源 |
| 42 | fjqbh | 机器编号 | varchar | 50 |  | √ | ' ' | 机器编号 |
| 43 | fbuyeremail | 购方邮箱 | varchar | 100 |  | √ | ' ' | 购方邮箱 |
| 44 | fterminalno | 终端号 | varchar | 50 |  | √ | ' ' | 终端号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sim_batch |  | fid |
| 2 | idx_sim_batch |  | finvoicecode,finvoiceno |

---

## 待开发票(旧)-分表 t_sim_batch_e

- **表名称：** 待开发票(旧)-分表
- **表名：** t_sim_batch_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbuyertype | 数据来源 | varchar | 30 |  | √ | ' ' | 数据来源,枚举: 1 :批量导入 3 :接口同步 4 :单据拆合 5 :作废重开 |
| 3 | finvalider | 作废人 | varchar | 50 |  | √ | ' ' | 作废人 |
| 4 | finvaliddate | 作废日期 | timestamp | 0 |  |  | null | 作废日期 |
| 5 | fcheckcode | 校验码 | varchar | 50 |  | √ | ' ' | 校验码 |
| 6 | foriginalinvoiceno | 原发票号码 | varchar | 50 |  | √ | ' ' | 原发票号码 |
| 7 | fredreason | 冲红原因 | varchar | 200 |  | √ | ' ' | 冲红原因 |
| 8 | foriginalinvoicetype | 原发票类型 | varchar | 30 |  | √ | ' ' | 原发票类型,枚举: 026 :增值税电子普通发票 004 :增值税专用发票 |
| 9 | fspecialflag | fspecialflag | varchar | 50 |  | √ | ' ' |  |
| 10 | fspecialredflag | 特殊红冲标志 | varchar | 50 |  | √ | ' ' | 特殊红冲标志,枚举: 0 :否 1 :是 |
| 11 | fredinfocode | 红字信息表编号 | varchar | 50 |  | √ | ' ' | 红字信息表编号 |
| 12 | foriginalissuetime | 原开票日期 | timestamp | 0 |  |  | null | 原开票日期 |
| 13 | fremainredamount | 剩余可红冲金额 | numeric | 23 | 10 | √ | 0.0000000000 | 剩余可红冲金额 |
| 14 | foriginalinvoicecode | 原发票代码 | varchar | 50 |  | √ | ' ' | 原发票代码 |
| 15 | fwxid | 微信ID | varchar | 50 |  | √ | ' ' | 微信ID |
| 16 | finventorymark | 清单标志 | varchar | 30 |  | √ | ' ' | 清单标志,枚举: 0 :无清单 1 :有清单 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sim_batch_e |  | fid |
| 2 | idx_sim_batch_e |  | finvaliddate |
