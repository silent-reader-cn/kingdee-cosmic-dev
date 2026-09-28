# 账单池-er_billingpool

## 附件信息-子表 t_er_billingattachinfo

- **表名称：** 附件信息-子表
- **表名：** t_er_billingattachinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fattstarttime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 3 | fattlargetxt | 长文本 | varchar | 255 |  |  | null | 长文本 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fattachserialno | 发票序列号 | varchar | 255 |  | √ | ' ' | 发票序列号 |
| 6 | fattsource | 来源 | varchar | 30 |  | √ | ' ' | 来源,枚举: 1 :发票云 2 :大模型 |
| 7 | fattachno | 附件序列号 | varchar | 80 |  | √ | ' ' | 附件序列号 |
| 8 | frotationangle | 旋转角度 | varchar | 30 |  | √ | ' ' | 旋转角度 |
| 9 | fattaffairdiscription | 事务描述 | varchar | 1024 |  |  | null | 事务描述 |
| 10 | fattheadcount | 人数 | int8 | 64 |  | √ | 0 | 人数 |
| 11 | fattcity | 城市 | varchar | 255 |  |  | null | 城市 |
| 12 | fattachurl | 附件 url | varchar | 512 |  |  | null | 附件 url |
| 13 | fattenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 14 | fattinvoiceentyid | 发票分录id | int8 | 64 |  | √ | 0 | 发票分录id |
| 15 | fattfrom | 出发地 | varchar | 255 |  |  | null | 出发地 |
| 16 | fattlargetxt_tag | 长文本_详情 | text | 0 |  |  | null | 长文本_详情 |
| 17 | fattachname | 附件名称 | varchar | 255 |  |  | null | 附件名称 |
| 18 | fattachremark | 备注 | varchar | 1024 |  |  | null | 备注 |
| 19 | foriginalname | 源文件名称 | varchar | 255 |  |  | null | 源文件名称 |
| 20 | fattto | 目的地 | varchar | 255 |  |  | null | 目的地 |
| 21 | fgathertime | 采集时间 | timestamp | 0 |  |  | null | 采集时间 |
| 22 | fattendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 23 | fattapplydate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 24 | fattstartdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 25 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 26 | fatttotalamount | 合计金额 | numeric | 23 | 10 | √ | 0 | 合计金额 |
| 27 | fsnapshoturl | 快照 url | varchar | 512 |  |  | null | 快照 url |
| 28 | fattachtype | 文件类型 | varchar | 30 |  | √ | ' ' | 文件类型,枚举: |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_billingattachinfo |  | fentryid |
| 2 | idx_er_billingattachinfo_fid |  | fid |

---

## 账单池-分表 t_er_billingpool_e

- **表名称：** 账单池-分表
- **表名：** t_er_billingpool_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | funauditmsg | 反审核意见 | varchar | 2000 |  |  | null | 反审核意见 |
| 3 | fisxbrl | xbrl | bpchar | 1 |  | √ | '0' | xbrl |
| 4 | finvoiceenddate | 通行日期止 | timestamp | 0 |  |  | null | 通行日期止 |
| 5 | fshowdetail | 账单明细 | bpchar | 1 |  | √ | '0' | 账单明细 |
| 6 | fisred | 红字发票 | varchar | 8 |  | √ | ' ' | 红字发票,枚举: 1 :是 0 :否 |
| 7 | falltaxrate | 税率(%) | varchar | 100 |  | √ | ' ' | 税率(%) |
| 8 | fvoucherno | 凭证编号 | varchar | 200 |  |  | null | 凭证编号 |
| 9 | frelbill | 关联单据 | varchar | 200 |  |  | null | 关联单据 |
| 10 | fspecialtypemark | 特定业务类型 | varchar | 4 |  | √ | '0' | 特定业务类型,枚举: 1 :成品油发票 2 :稀土发票 3 :机动车发票 4 :农产品收购发票 5 :石脑油发票 6 :卷烟发票 7 :建筑服务发票 8 :货物运输服务发票 9 :不动产销售服务发票 10 :不动产经营租赁服务 11 :代收车船税发票 12 :旅客运输服务发票 13 :自产农产品销售发票 14 :通行费发票 15 :医疗服务（住院）发票 16 :医疗服务（门诊）发票 17 :拖拉机和联合收割机发票 18 :二手车发票 19 :光伏收购发票 20 :出口发票 21 :农产品发票 22 :稀土矿产品发票 23 :稀土产成品发票 24 :铁路电子客票 25 :航空运输电子客票行程单 26 :电子烟 27 :正常开具 28 :反向开具 |
| 11 | fenginenum | 发动机号码 | varchar | 20 |  | √ | ' ' | 发动机号码 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | finvoicestartdate | 通行日期起 | timestamp | 0 |  |  | null | 通行日期起 |
| 14 | fattachmentcount | 附件数 | int4 | 32 |  | √ | 0 | 附件数 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | ftrdbizno | 第三方业务编号 | varchar | 160 |  | √ | ' ' | 第三方业务编号 |
| 17 | fformid | 表单id | varchar | 20 |  | √ | ' ' | 表单id |
| 18 | fremark | 备注 | varchar | 2000 |  |  | null | 备注 |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fvincode | 车辆识别代号 | varchar | 50 |  | √ | ' ' | 车辆识别代号 |
| 21 | ftaxauthority | 税务机关 | varchar | 30 |  | √ | ' ' | 税务机关 |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | fshowtrip | 行程信息 | bpchar | 1 |  | √ | '0' | 行程信息 |
| 24 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 25 | fisexpensesync | 报销单同步 | bpchar | 1 |  | √ | '0' | 报销单同步 |
| 26 | fvehicletype | 车辆类型 | varchar | 50 |  | √ | ' ' | 车辆类型 |
| 27 | fistartcity | 出发城市 | varchar | 20 |  | √ | ' ' | 出发城市 |
| 28 | fvehicleremark | 备注 | varchar | 2000 |  | √ | ' ' | 备注 |
| 29 | ftimegetoff | 下车时间 | timestamp | 0 |  |  | null | 下车时间 |
| 30 | fblockchain | 区块链 | bpchar | 1 |  | √ | ' ' | 区块链 |
| 31 | finvaddr | 发票下载地址 | varchar | 1000 |  |  | null | 发票下载地址 |
| 32 | fmodified | 已修改 | bpchar | 1 |  | √ | '0' | 已修改 |
| 33 | fshowvehicle | 车辆信息 | bpchar | 1 |  | √ | '0' | 车辆信息 |
| 34 | fprojecttype | 业务分类 | int8 | 64 |  | √ | 0 | [业务分类 er_projecttype](../em_files/er_projecttype.md) |
| 35 | fendorsement | 签注 | varchar | 255 |  |  | null | 签注 |
| 36 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 37 | fidestcity | 目的城市 | varchar | 20 |  | √ | ' ' | 目的城市 |
| 38 | finvoiceairtime | 飞机乘机时间 | varchar | 16 |  | √ | ' ' | 飞机乘机时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_billingpool_auditer |  | fauditorid |
| 2 | pk_t_er_billingpool_e |  | fid |

---

## 账单池-多语言表 t_er_billingpool_l

- **表名称：** 账单池-多语言表
- **表名：** t_er_billingpool_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fapplierpositionstr | 职位文本 | varchar | 100 |  |  | ' ' | 职位文本 |
| 3 | frelbilltype | 关联单据类型 | varchar | 200 |  |  | ' ' | 关联单据类型 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_billingpool_l_fid |  | fid |
| 2 | pk_t_er_billingpool_l |  | fpkid |

---

## 干系人-多选基础资料表 t_er_billingpoolower

- **表名称：** 干系人-多选基础资料表
- **表名：** t_er_billingpoolower

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_billingpoolower |  | fid |
| 2 | pk_er_billingpoolower |  | fpkid |

---

## 记账信息-子表 t_er_billingpool_voucher

- **表名称：** 记账信息-子表
- **表名：** t_er_billingpool_voucher

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fvouchertype | 凭证类型 | varchar | 60 |  | √ | ' ' | 凭证类型 |
| 3 | fvoucherid | 凭证id | int8 | 64 |  | √ | 0 | 凭证id |
| 4 | fvouchercreator | 凭证制单人 | varchar | 200 |  |  | null | 凭证制单人 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fvouchernum | 凭证字号 | varchar | 200 |  |  | null | 凭证字号 |
| 7 | fissmallreim | 大票小报 | bpchar | 1 |  | √ | '0' | 大票小报 |
| 8 | frelentryid | 关联分录id | int8 | 64 |  | √ | 0 | 关联分录id |
| 9 | fperiod | 入账期间 | timestamp | 0 |  |  | null | 入账期间 |
| 10 | frelbills | 关联单据编号 | varchar | 200 |  |  | null | 关联单据编号 |
| 11 | fentityid | 单据实体标识 | varchar | 50 |  | √ | ' ' | 单据实体标识 |
| 12 | frelbillid | 关联单据id | int8 | 64 |  | √ | 0 | 关联单据id |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_billingpool_voucher |  | fentryid |
| 2 | idx_billingpool_voucher_billno |  | frelbills |

---

## 账单明细-子表 t_er_billingpool_detail

- **表名称：** 账单明细-子表
- **表名：** t_er_billingpool_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentryamount | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 3 | ftaxrate | 税率(%) | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 4 | fentryoribalanceamount | 可用金额 | numeric | 23 | 10 | √ | 0 | 可用金额 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 7 | fnum | 数量 | int8 | 64 |  | √ | 0 | 数量 |
| 8 | fgoodsname | 商品名称 | varchar | 50 |  | √ | ' ' | 商品名称 |
| 9 | fspecmodel | 规格型号 | varchar | 600 |  | √ | ' ' | 规格型号 |
| 10 | fentrytaxamount | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 11 | fentryoriusedamount | 已用金额 | numeric | 23 | 10 | √ | 0 | 已用金额 |
| 12 | fentrytaxrate | 税率(%) | varchar | 10 |  | √ | ' ' | 税率(%) |
| 13 | fentryremark | 备注 | varchar | 2000 |  |  | null | 备注 |
| 14 | ftaxclasscode | 税收分类编码 | varchar | 50 |  | √ | ' ' | 税收分类编码 |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 16 | funit | 单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 17 | fentrynotaxamount | 不含税金额 | numeric | 23 | 10 | √ | 0 | 不含税金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_billingpool_detail |  | fentryid |
| 2 | idx_er_billingpool_balancea |  | fentryoribalanceamount |

---

## 账单池-主表 t_er_billingpool

- **表名称：** 账单池-主表
- **表名：** t_er_billingpool

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fwithholdingtaxrate | 预扣税率 | numeric | 23 | 10 | √ | 0 | 预扣税率 |
| 3 | fbillpooltype | 账单类型 | int8 | 64 |  | √ | 0 | [账单类型 er_bd_billingpool_type](../basedata_files/er_bd_billingpool_type.md) |
| 4 | forgid | 部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | ftotalamount | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 6 | fcostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | foffset | 可抵扣(发票) | bpchar | 1 |  | √ | '0' | 可抵扣(发票) |
| 8 | fbuyeraddressphone | 地址与电话 | varchar | 200 |  |  | null | 地址与电话 |
| 9 | fpassengername | 旅客 | varchar | 200 |  |  | null | 旅客 |
| 10 | fapplierpositionstr | fapplierpositionstr | varchar | 100 |  | √ | ' ' |  |
| 11 | finvoicecode | 发票代码 | varchar | 129 |  | √ | ' ' | 发票代码 |
| 12 | foribalanceamount | 可用金额 | numeric | 23 | 10 | √ | 0 | 可用金额 |
| 13 | fbasealltaxrate | 税率(%) | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 14 | fcity | 发票所在地 | varchar | 100 |  | √ | ' ' | 发票所在地 |
| 15 | fimageno | 影像编号 | varchar | 50 |  | √ | ' ' | 影像编号 |
| 16 | foutreason | 转出原因 | varchar | 2000 |  |  | null | 转出原因,枚举: a :免税项目用 b :集体福利、个人消费 c :非正常损失 d :简易计税方法征税项目用 e :免抵退税办法不得抵扣的进项税额 f :纳税检查调减进项税额 g :红字专用发票信息表注明的进项税额 h :上期留抵税额抵减欠税 i :上期留抵税额退税 j :其他应作进项税额转出的情形 |
| 17 | finvoiceno | 发票号码 | varchar | 129 |  | √ | ' ' | 发票号码 |
| 18 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 19 | fexpirypaydate | 付款到期日 | timestamp | 0 |  |  | null | 付款到期日 |
| 20 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 21 | fname | 名称 | varchar | 2000 |  | √ | ' ' | 名称 |
| 22 | fgathertotalamount | 价税合计（采集） | numeric | 23 | 10 | √ | 0 | 价税合计（采集） |
| 23 | fnotaxamount | 不含税金额 | numeric | 23 | 10 | √ | 0 | 不含税金额 |
| 24 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 E :已审核 H :废弃 J :报销中 K :已报销 |
| 25 | fserialno | 发票序列号 | varchar | 80 |  | √ | ' ' | 发票序列号 |
| 26 | fbuyeropenbank | 开户行及账号 | varchar | 100 |  | √ | ' ' | 开户行及账号 |
| 27 | ftaxdetails | 多税率信息 | varchar | 500 |  | √ | ' ' | 多税率信息 |
| 28 | fseatgrade | 座位等级 | varchar | 20 |  | √ | ' ' | 座位等级 |
| 29 | fisgenvoucher | 生成凭证 | bpchar | 1 |  | √ | '0' | 生成凭证 |
| 30 | foffsetamount | 抵扣税额 | numeric | 23 | 10 | √ | 0 | 抵扣税额 |
| 31 | fvalidateorg | 校验组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 32 | foffsetexpense | 可抵扣(报销) | varchar | 8 |  | √ | ' ' | 可抵扣(报销) |
| 33 | fvehiclenum | 航班号/车次 | varchar | 50 |  | √ | ' ' | 航班号/车次 |
| 34 | fcustomeridnumber | 身份证 | varchar | 30 |  | √ | ' ' | 身份证 |
| 35 | finvoicetype | 发票类型 | int8 | 64 |  | √ | 0 | [发票类型(发票云) er_invoicetype](../basedata_files/er_invoicetype.md) |
| 36 | frelbilltype | 关联单据类型 | varchar | 200 |  | √ | ' ' | 关联单据类型 |
| 37 | fvehplate | 车牌号 | varchar | 20 |  | √ | ' ' | 车牌号 |
| 38 | fmodified | fmodified | bpchar | 1 |  | √ | '0' |  |
| 39 | fcountrystr | 国家 | varchar | 500 |  | √ | ' ' | 国家 |
| 40 | fissequence | 连号 | bpchar | 1 |  | √ | '0' | 连号 |
| 41 | ftimegeton | 上车时间 | timestamp | 0 |  |  | null | 上车时间 |
| 42 | fcompanyid | 公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 43 | fcountry | 国家 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 44 | freceiptdate | 收票日期 | timestamp | 0 |  |  | null | 收票日期 |
| 45 | ftel | 联系方式 | varchar | 20 |  | √ | ' ' | 联系方式 |
| 46 | finvoicestatus | 账单状态 | varchar | 20 |  | √ | ' ' | 账单状态,枚举: normal :正常 outOfControl :失控 voided :作废 redInvoice :红冲 partialRed :部分红冲 fullRed :全额红冲 redPending :红字发票待确认 abnormal :异常 rescheduled :改签 ticketSale :售票 ticketRefund :退票 |
| 47 | fbrand | 厂牌型号 | varchar | 20 |  | √ | ' ' | 厂牌型号 |
| 48 | fidestprovince | 目的省份 | varchar | 20 |  | √ | ' ' | 目的省份 |
| 49 | fsource | 来源 | varchar | 16 |  | √ | ' ' | 来源,枚举: 0 :手动新增 1 :金蝶发票云 6 :excel导入 2 :支付宝 |
| 50 | fbtaxpayerid | 纳税人识别号 | varchar | 50 |  | √ | ' ' | 纳税人识别号 |
| 51 | fusage | 用途 | varchar | 2000 |  |  | null | 用途 |
| 52 | fothertotaltaxamount | 其他税费 | numeric | 23 | 10 | √ | 0 | 其他税费 |
| 53 | fcurwithholdingtaxamount | 预扣税额（本位币） | numeric | 23 | 10 | √ | 0 | 预扣税额（本位币） |
| 54 | fselleraddressphone | 地址与电话 | varchar | 100 |  | √ | ' ' | 地址与电话 |
| 55 | finsurancepremium | 保险费 | numeric | 23 | 10 | √ | 0 | 保险费 |
| 56 | foricurrency | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 57 | fcheckresult | 校验结果 | varchar | 2000 |  |  | null | 校验结果 |
| 58 | fairconstfee | 民航发展基金 | numeric | 23 | 10 | √ | 0 | 民航发展基金 |
| 59 | finvoicedate | 发票/账单日期 | timestamp | 0 |  |  | null | 发票/账单日期 |
| 60 | fbuyerorg | 购方名称 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 61 | fregion | 地域 | varchar | 100 |  | √ | ' ' | 地域,枚举: 1 :国内 2 :国际 |
| 62 | finvoicefuelsurcharge | 燃油附加费 | numeric | 23 | 10 | √ | 0 | 燃油附加费 |
| 63 | fregnum | 登记证号 | varchar | 50 |  | √ | ' ' | 登记证号 |
| 64 | fcostcompanyid | 费用承担公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 65 | fismutilreimburse | 多次报销 | bpchar | 1 |  | √ | '0' | 多次报销 |
| 66 | fseller | 销方名称 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 67 | fgathertaxamount | 税额（采集） | numeric | 23 | 10 | √ | 0 | 税额（采集） |
| 68 | ftripto | 目的地 | varchar | 30 |  | √ | ' ' | 目的地 |
| 69 | fbuyerbankaccount | 购方银行账号 | varchar | 100 |  | √ | ' ' | 购方银行账号 |
| 70 | fgatherbuyer | 购方名称（采集） | varchar | 250 |  | √ | ' ' | 购方名称（采集） |
| 71 | foutamount | 转出金额 | numeric | 23 | 10 | √ | 0 | 转出金额 |
| 72 | fgatherseller | 销方名称（采集） | varchar | 250 |  | √ | ' ' | 销方名称（采集） |
| 73 | fexpenseitem | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 74 | fcurrency | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 75 | fgather | 采集人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 76 | fstaxpayerid | 纳税人识别号 | varchar | 50 |  | √ | ' ' | 纳税人识别号 |
| 77 | fistartprovince | 出发省份 | varchar | 20 |  | √ | ' ' | 出发省份 |
| 78 | ftripfrom | 出发地 | varchar | 30 |  | √ | ' ' | 出发地 |
| 79 | foriusedamount | 已用金额 | numeric | 23 | 10 | √ | 0 | 已用金额 |
| 80 | fapplierid | 申请人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 81 | fnodeductionreason | 不抵扣原因 | varchar | 2 |  | √ | ' ' | 不抵扣原因,枚举: 1 :用于非应税项目 2 :用于免税项目 3 :用于集体福利或个人消费 4 :遭受非正常损失 5 :其他 |
| 82 | fwithholdingtaxamount | 预扣税额 | numeric | 23 | 10 | √ | 0 | 预扣税额 |
| 83 | fgatherdate | 采集日期 | timestamp | 0 |  |  | null | 采集日期 |
| 84 | fselleropenbank | 开户行及账号 | varchar | 200 |  |  | null | 开户行及账号 |
| 85 | fproxymark | 代开 | bpchar | 1 |  | √ | '0' | 代开 |
| 86 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 87 | fcheckstatus | 查验状态 | bpchar | 1 |  | √ | ' ' | 查验状态,枚举: 1 :通过 2 :不通过 3 :未查验 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_billingpool |  | fid |
| 2 | idx_er_billingpool_invoice |  | finvoicecode,finvoiceno |
| 3 | idx_er_billingpool_fserialno |  | fserialno |
