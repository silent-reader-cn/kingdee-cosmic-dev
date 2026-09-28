# 红字信息表-sim_red_info

## 红字信息表-主表 t_sim_red_info

- **表名称：** 红字信息表-主表
- **表名：** t_sim_red_info

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbuyeraddr | 购方地址电话 | varchar | 100 |  | √ | ' ' | 购方地址电话 |
| 3 | fdrawer | 开票人： | varchar | 50 |  | √ | ' ' | 开票人： |
| 4 | ftaxorg | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | ftaxbureauaudittime | 税局审核日期： | timestamp | 0 |  |  | null | 税局审核日期： |
| 6 | ftotalamount | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 7 | forg | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 9 | fbatchbelong | 申请批次号 | varchar | 50 |  | √ | ' ' | 申请批次号 |
| 10 | fsalerbankacc | fsalerbankacc | varchar | 50 |  | √ | ' ' |  |
| 11 | fapplyreason | 备注 | varchar | 100 |  | √ | ' ' | 备注 |
| 12 | fsaleraddr | 销方地址电话 | varchar | 100 |  | √ | ' ' | 销方地址电话 |
| 13 | finvoicecode | 发票代码 | varchar | 20 |  | √ | ' ' | 发票代码 |
| 14 | fspecialtype | 特殊票种 | varchar | 50 |  | √ | ' ' | 特殊票种,枚举: 00 :非特殊票种 02 :收购 06 :抵扣通行费 07 :不抵扣通行费 08 :成品油 |
| 15 | fbuyername | 购方名称 | varchar | 100 |  | √ | ' ' | 购方名称 |
| 16 | finvoiceno | 发票号码 | varchar | 15 |  | √ | ' ' | 发票号码 |
| 17 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 18 | fsalertaxno | 销方纳税人识别号 | varchar | 50 |  | √ | ' ' | 销方纳税人识别号 |
| 19 | finfotype | 信息表类型 | varchar | 30 |  | √ | '0' | 信息表类型,枚举: 0 :非特殊票种 2 :机动车（涉及退货和开具错误等，合格证退回） 3 :机动车（仅涉及销售折让，合格证不退回）） |
| 20 | finfodate | 填开日期 | timestamp | 0 |  |  | null | 填开日期 |
| 21 | fbillstatus | 单据状态 | varchar | 10 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 D :无需审批 |
| 22 | fsubmitterid | 申请人： | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 23 | foriginalinvoiceno | 原发票号码 | varchar | 15 |  | √ | ' ' | 原发票号码 |
| 24 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 25 | fauditdate | 审核日期： | timestamp | 0 |  |  | null | 审核日期： |
| 26 | freason | 申请事由： | varchar | 200 |  | √ | ' ' | 申请事由： |
| 27 | fdeduction | 扣除额 | numeric | 23 | 10 | √ | 0 | 扣除额 |
| 28 | fissuedate | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 29 | fsalertelno | fsalertelno | varchar | 50 |  | √ | ' ' |  |
| 30 | forderno | 开票流水号 | varchar | 50 |  | √ | ' ' | 开票流水号 |
| 31 | fbillnumber | fbillnumber | varchar | 50 |  | √ | ' ' |  |
| 32 | fmergelable | 合并标识 | varchar | 50 |  | √ | ' ' | 合并标识 |
| 33 | finvoicetype | 发票类型 | varchar | 30 |  | √ | ' ' | 发票类型,枚举: 028 :增值税电子专用发票 004 :增值税纸质专用发票 |
| 34 | foriginalinvoicecode | 原发票代码 | varchar | 20 |  | √ | ' ' | 原发票代码 |
| 35 | fbuyerbank | 购方开户行及账号 | varchar | 100 |  | √ | ' ' | 购方开户行及账号 |
| 36 | fsalername | 销方名称 | varchar | 100 |  | √ | ' ' | 销方名称 |
| 37 | fbuyerbankacc | fbuyerbankacc | varchar | 50 |  | √ | ' ' |  |
| 38 | fauditorid | 审核人： | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 39 | fterminalno | 终端号 | varchar | 50 |  | √ | ' ' | 终端号 |
| 40 | fpayee | 收款人： | varchar | 50 |  | √ | ' ' | 收款人： |
| 41 | fhsbz | 是否含税 | varchar | 30 |  | √ | ' ' | 是否含税,枚举: 0 :不含税 1 :含税 |
| 42 | fagent | fagent | varchar | 50 |  | √ | ' ' |  |
| 43 | fbuyertelno | fbuyertelno | varchar | 50 |  | √ | ' ' |  |
| 44 | ftotaltax | 合计税额 | numeric | 23 | 10 | √ | 0.0000000000 | 合计税额 |
| 45 | fstatus | 信息表状态 | varchar | 30 |  | √ | ' ' | 信息表状态,枚举: 1 :未上传 2 :审核失败 3 :审核成功 4 :已开票 |
| 46 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 47 | freviewer | 复核人： | varchar | 50 |  | √ | ' ' | 复核人： |
| 48 | fbuyertaxno | 购方纳税人识别号 | varchar | 50 |  | √ | ' ' | 购方纳税人识别号 |
| 49 | fsalerbank | 销方开户行及账号 | varchar | 100 |  | √ | ' ' | 销方开户行及账号 |
| 50 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 51 | finfocode | 信息表编号 | varchar | 32 |  | √ | ' ' | 信息表编号 |
| 52 | fapplicant | 申请方 | varchar | 30 |  | √ | ' ' | 申请方,枚举: 2 :销方申请 1 :购方申请-未抵扣 0 :购方申请-已抵扣 |
| 53 | finfosource | 信息表来源 | varchar | 30 |  | √ | ' ' | 信息表来源,枚举: 1 :手工新增 2 :税局下载 3 :批量导入 4 :API接口 5 :单据开票 6 :单据手工输入 |
| 54 | foriginaldeduction | 扣除额 | numeric | 23 | 10 | √ | 0.0000000000 | 扣除额 |
| 55 | fsubmitdate | 申请日期： | timestamp | 0 |  |  | null | 申请日期： |
| 56 | foriginalissuetime | 原开票日期 | timestamp | 0 |  |  | null | 原开票日期 |
| 57 | finvoiceamount | 合计金额 | numeric | 23 | 10 | √ | 0.0000000000 | 合计金额 |
| 58 | finfoserialno | 信息表流水号 | varchar | 30 |  | √ | ' ' | 信息表流水号 |
| 59 | fapplytaxno | 申请方税号 | varchar | 50 |  | √ | ' ' | 申请方税号 |
| 60 | fsystemsource | 数据系统来源 | varchar | 50 |  | √ | ' ' | 数据系统来源 |
| 61 | finfostatus | 申请返回状态 | varchar | 30 |  | √ | ' ' | 申请返回状态,枚举: TZD0000 :审核通过 TZD0500 :未上传 TZD0061 :重复上传 TZD0071 :待查证 TZD0072 :已核销,待查证 TZD0073 :已核销,查证未通过,待处理 TZD0074 :已核销 TZD0075 :核销后激活 B900071 :重复上传 |
| 62 | fmaintaxrate | 综合税率 | varchar | 10 |  | √ | ' ' | 综合税率 |
| 63 | fjqbh | 机器编号 | varchar | 50 |  | √ | ' ' | 机器编号 |
| 64 | finventorymark | 清单标志 | varchar | 30 |  | √ | ' ' | 清单标志,枚举: 0 :无清单 1 :有清单 |
| 65 | fstatusdescribe | 信息表状态描述 | varchar | 50 |  | √ | ' ' | 信息表状态描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sim_red_info |  | fid |
| 2 | idx_sim_red_info_org |  | forg |
| 3 | idx_sim_red_info_code |  | finfocode |
| 4 | idx_sim_red_info_time |  | fcreatetime |

---

## 红字信息表明细-子表 t_sim_red_info_item

- **表名称：** 红字信息表明细-子表
- **表名：** t_sim_red_info_item

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsimplegoodsname | 分类编码简称 | varchar | 50 |  | √ | ' ' | 分类编码简称 |
| 3 | ftaxamount | 含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 含税金额 |
| 4 | ftaxrate | 税率 | varchar | 30 |  | √ | ' ' | 税率,枚举: 0 :0% 0.01 :1% 0.03 :3% 0.05 :5% 0.06 :6% 0.09 :9% 0.10 :10% 0.11 :11% 0.13 :13% 0.15 :15% 0.16 :16% 0.17 :17% |
| 5 | frowtype | 发票行性质 | varchar | 30 |  | √ | ' ' | 发票行性质,枚举: 0 :明细行 1 :折扣行 2 :被折扣行 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | ftaxflag | 含税标识(弃用) | varchar | 10 |  | √ | ' ' | 含税标识(弃用) |
| 8 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 9 | fzerotaxmark | 零税率标识 | varchar | 2 |  | √ | ' ' | 零税率标识 |
| 10 | ftaxpremark | 税收优惠政策标识 | varchar | 2 |  | √ | ' ' | 税收优惠政策标识 |
| 11 | fnum | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 12 | ftaxunitprice | 含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 含税单价 |
| 13 | funitprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 14 | fgoodscode | 税收分类编码 | varchar | 30 |  | √ | ' ' | 税收分类编码 |
| 15 | fgoodsname | 商品名称 | varchar | 100 |  | √ | ' ' | 商品名称 |
| 16 | fspecification | 规格 | varchar | 50 |  | √ | ' ' | 规格 |
| 17 | ftax | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 18 | fbillsourceid | 单据来源id | varchar | 50 |  | √ | ' ' | 单据来源id |
| 19 | fzzstsgl | 增值税特殊管理 | varchar | 500 |  | √ | ' ' | 增值税特殊管理 |
| 20 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 21 | funit | 单位 | varchar | 50 |  | √ | ' ' | 单位 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sim_red_info_item |  | fentryid |
| 2 | idx_sim_red_info_item_fk |  | fid |
| 3 | idx_sim_red_info_no |  | fseq |
