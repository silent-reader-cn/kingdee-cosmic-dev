# 用车申请单-er_dailyvehiclebill

## 用车申请单-主表 t_er_dailyvehiclebill

- **表名称：** 用车申请单-主表
- **表名：** t_er_dailyvehiclebill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | funauditmsg | 反审核意见 | varchar | 1000 |  | √ | ' ' | 反审核意见 |
| 3 | finvokeinvoicecloud | 与发票云交互 | bpchar | 1 |  | √ | '0' | 与发票云交互 |
| 4 | ftel | 联系方式 | varchar | 50 |  | √ | ' ' | 联系方式 |
| 5 | fdestinationcity | 目的城市 | int8 | 64 |  | √ | 0 | 行政区划 bd_admindivision |
| 6 | forgid | 部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fcostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fvehiclenumber | 用车次数 | int8 | 64 |  | √ | 1 | 用车次数 |
| 9 | fheadproject | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstdcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 12 | fenddate | 用车日期.结束 | timestamp | 0 |  |  | null | 用车日期.结束 |
| 13 | fattachmentcount | 附件数 | int4 | 32 |  | √ | 0 | 附件数 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fvehiclecity | 用车城市 | int8 | 64 |  | √ | 0 | 行政区划 bd_admindivision |
| 16 | ftrdbizno | 第三方业务编号 | varchar | 160 |  | √ | ' ' | 第三方业务编号 |
| 17 | fcostcompanyid | 费用承担公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 18 | ffrom | 出发地 | varchar | 30 |  | √ | ' ' | 出发地 |
| 19 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 20 | fformid | 表单ID | varchar | 50 |  | √ | ' ' | 表单ID,枚举: er_tripreqbill :出差申请单 er_loanbill :出差借款单 er_tripreimbursebill :差旅费报销单 er_dailyapplybill :费用申请单 er_dailyloanbill :借款单 er_dailyreimbursebill :费用报销单 er_repaymentbill :还款单 er_dailyvehiclebill :日常用车申请单 |
| 21 | fto | 目的地 | varchar | 30 |  | √ | ' ' | 目的地 |
| 22 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | fbillstatus | 单据状态 | varchar | 30 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :审核中 D :审核未通过 E :审核通过 |
| 24 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 25 | fdescription | 用车说明 | varchar | 600 |  | √ | ' ' | 用车说明 |
| 26 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 27 | fisenableinvoice | 启用发票云 | bpchar | 1 |  | √ | '0' | 启用发票云 |
| 28 | fvehicletype | 用车类型 | varchar | 50 |  | √ | '2' | 用车类型,枚举: 2 :公务出行用车 4 :周末/节假日加班用车 |
| 29 | fapplierposition | fapplierposition | varchar | 50 |  | √ | ' ' |  |
| 30 | fapplierid | 申请人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 31 | fstartdate | 用车日期.开始 | timestamp | 0 |  |  | null | 用车日期.开始 |
| 32 | fbizdate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 33 | fnextauditor | 下一步审核人 | varchar | 50 |  | √ | ' ' | 下一步审核人 |
| 34 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 35 | fneedimagescan | 需要影像扫描 | bpchar | 1 |  | √ | '0' | 需要影像扫描,枚举: 1 :是 2 :否 |
| 36 | fcompanyid | 申请人公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_vehicle_fbillno_status |  | fbillno,fbillstatus |
| 2 | pk_t_er_dailyvehiclebill |  | fid |

---

## 发票云附件-子表 t_er_invoiceattachinfo

- **表名称：** 发票云附件-子表
- **表名：** t_er_invoiceattachinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fattstarttime | fattstarttime | timestamp | 0 |  |  | null |  |
| 3 | fattlargetxt | fattlargetxt | varchar | 255 |  |  | null |  |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fattachserialno | fattachserialno | varchar | 255 |  | √ | ' ' |  |
| 6 | fattsource | fattsource | varchar | 30 |  | √ | ' ' |  |
| 7 | fattachno | 附件序列号 | varchar | 80 |  | √ | ' ' | 附件序列号 |
| 8 | frotationangle | 旋转角度 | varchar | 30 |  |  | null | 旋转角度 |
| 9 | fattaffairdiscription | fattaffairdiscription | varchar | 1024 |  |  | null |  |
| 10 | fattheadcount | fattheadcount | int8 | 64 |  | √ | 0 |  |
| 11 | fattcity | fattcity | varchar | 255 |  |  | null |  |
| 12 | fattachurl | 附件 url | varchar | 512 |  |  | null | 附件 url |
| 13 | fattenddate | fattenddate | timestamp | 0 |  |  | null |  |
| 14 | fattinvoiceentyid | fattinvoiceentyid | int8 | 64 |  | √ | 0 |  |
| 15 | fattfrom | fattfrom | varchar | 255 |  |  | null |  |
| 16 | fattlargetxt_tag | fattlargetxt_tag | text | 0 |  |  | null |  |
| 17 | fattachname | 附件名称 | varchar | 255 |  |  | null | 附件名称 |
| 18 | fattachremark | 备注 | varchar | 1024 |  |  | null | 备注 |
| 19 | foriginalname | 源文件名称 | varchar | 255 |  |  | null | 源文件名称 |
| 20 | fattto | fattto | varchar | 255 |  |  | null |  |
| 21 | fgathertime | 采集时间 | timestamp | 0 |  |  | null | 采集时间 |
| 22 | fattendtime | fattendtime | timestamp | 0 |  |  | null |  |
| 23 | fattapplydate | fattapplydate | timestamp | 0 |  |  | null |  |
| 24 | fattstartdate | fattstartdate | timestamp | 0 |  |  | null |  |
| 25 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 26 | fatttotalamount | fatttotalamount | numeric | 23 | 10 | √ | 0 |  |
| 27 | fsnapshoturl | 快照 url | varchar | 512 |  |  | null | 快照 url |
| 28 | fattachtype | 文件类型 | varchar | 30 |  |  | null | 文件类型,枚举: |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_invoiceattachinfo |  | fentryid |
| 2 | idx_er_invoiceattachinfo_fid |  | fid |

---

## 项目干系人-多选基础资料表 t_er_dailyvehicleower

- **表名称：** 项目干系人-多选基础资料表
- **表名：** t_er_dailyvehicleower

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
| 1 | idx_er_dailyvehicleower_fid |  | fid |
| 2 | pk_er_dailyvehicleower |  | fpkid |

---

## 用车申请单-多语言表 t_er_dailyvehiclebill_l

- **表名称：** 用车申请单-多语言表
- **表名：** t_er_dailyvehiclebill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fapplierposition | 职位文本 | varchar | 50 |  | √ | ' ' | 职位文本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_vehiclebill_l_fid_l |  | fid,flocaleid |
| 2 | pk_t_er_dailyvehiclebill_l |  | fpkid |
