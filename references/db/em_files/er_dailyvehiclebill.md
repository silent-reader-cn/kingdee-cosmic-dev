# 用车申请单-er_dailyvehiclebill

## 用车申请单-主表 t_er_dailyvehiclebill

- **表名称：** 用车申请单-主表
- **表名：** t_er_dailyvehiclebill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | finvokeinvoicecloud | 是否与发票云交互 | bpchar | 1 |  | √ | '0' | 是否与发票云交互 |
| 3 | ftel | 联系方式 | varchar | 50 |  | √ | ' ' | 联系方式 |
| 4 | forgid | 部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fcostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fvehiclenumber | 用车次数 | int8 | 64 |  | √ | 1 | 用车次数 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstdcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 9 | fenddate | 用车日期.结束 | timestamp | 0 |  |  | null | 用车日期.结束 |
| 10 | fattachmentcount | 附件数 | int4 | 32 |  | √ | 0 | 附件数 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fvehiclecity | 用车城市 | int8 | 64 |  | √ | 0 | 行政区划 bd_admindivision |
| 13 | fcostcompanyid | 费用承担公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 14 | ffrom | 出发地 | varchar | 30 |  | √ | ' ' | 出发地 |
| 15 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 16 | fformid | 表单ID | varchar | 50 |  | √ | ' ' | 表单ID,枚举: er_tripreqbill :出差申请单 er_loanbill :出差借款单 er_tripreimbursebill :差旅费报销单 er_dailyapplybill :费用申请单 er_dailyloanbill :借款单 er_dailyreimbursebill :费用报销单 er_repaymentbill :还款单 er_dailyvehiclebill :日常用车申请单 |
| 17 | fto | 目的地 | varchar | 30 |  | √ | ' ' | 目的地 |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fbillstatus | 单据状态 | varchar | 30 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :审核中 D :审核未通过 E :审核通过 |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fdescription | 用车说明 | varchar | 600 |  | √ | ' ' | 用车说明 |
| 22 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 23 | fisenableinvoice | 是否启用发票云 | bpchar | 1 |  | √ | '0' | 是否启用发票云 |
| 24 | fvehicletype | 用车类型 | varchar | 50 |  | √ | '2' | 用车类型,枚举: 2 :公务出行用车 4 :周末/节假日加班用车 |
| 25 | fapplierposition | fapplierposition | varchar | 50 |  | √ | ' ' |  |
| 26 | fapplierid | 申请人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 27 | fstartdate | 用车日期.开始 | timestamp | 0 |  |  | null | 用车日期.开始 |
| 28 | fbizdate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 29 | fnextauditor | 下一步审核人 | varchar | 50 |  | √ | ' ' | 下一步审核人 |
| 30 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 31 | fneedimagescan | 需要影像扫描 | bpchar | 1 |  | √ | '0' | 需要影像扫描,枚举: 1 :是 2 :否 |
| 32 | fcompanyid | 申请人公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |

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
| 2 | fattachname | 附件名称 | varchar | 255 |  |  | null | 附件名称 |
| 3 | fattachurl | 附件 url | varchar | 512 |  |  | null | 附件 url |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fattachremark | 备注 | varchar | 1024 |  |  | null | 备注 |
| 6 | fattachno | 附件序列号 | varchar | 80 |  | √ | ' ' | 附件序列号 |
| 7 | frotationangle | 旋转角度 | varchar | 30 |  |  | null | 旋转角度 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | foriginalname | 源文件名称 | varchar | 255 |  |  | null | 源文件名称 |
| 10 | fgathertime | 采集时间 | timestamp | 0 |  |  | null | 采集时间 |
| 11 | fsnapshoturl | 快照 url | varchar | 512 |  |  | null | 快照 url |
| 12 | fattachtype | 文件类型 | varchar | 30 |  |  | null | 文件类型,枚举: |

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
