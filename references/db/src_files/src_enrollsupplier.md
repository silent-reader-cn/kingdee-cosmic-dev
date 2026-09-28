# 报名供应商(后台元数据)-src_enrollsupplier

## 附件-附件表 t_src_enrollsupplier_fj

- **表名称：** 附件-附件表
- **表名：** t_src_enrollsupplier_fj

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 附件字段实体 bd_attachment |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_enrollsupplier_fj_eid |  | fentryid |
| 2 | pk_src_enrollsupplier_fj |  | fpkid |
| 3 | idx_src_enrollsupplier_fj_bid |  | fbasedataid |

---

## 报名供应商(后台元数据)-主表 t_src_enrollsupplier

- **表名称：** 报名供应商(后台元数据)-主表
- **表名：** t_src_enrollsupplier

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 2 | frisknum | 风险数 | int4 | 32 |  | √ | 0 | 风险数 |
| 3 | faddress | 联系地址 | varchar | 100 |  | √ | ' ' | 联系地址 |
| 4 | fisaptpush | 资质预审下达否 | bpchar | 1 |  | √ | '0' | 资质预审下达否 |
| 5 | fsocietycreditcode | 统一社会信用代码 | varchar | 255 |  | √ | ' ' | 统一社会信用代码 |
| 6 | fisbidpush | 评标任务下达否 | bpchar | 1 |  | √ | '0' | 评标任务下达否 |
| 7 | fisselect | 是否推荐 | bpchar | 1 |  | √ | '0' | 是否推荐 |
| 8 | fseq | 序号 | int8 | 64 |  | √ | 0 | 序号 |
| 9 | fnote | 推荐原因说明 | varchar | 100 |  | √ | ' ' | 推荐原因说明 |
| 10 | fenrollemail | fenrollemail | varchar | 50 |  | √ | ' ' |  |
| 11 | fapplytime | 报名时间 | timestamp | 0 |  |  | null | 报名时间 |
| 12 | fisaptitude | 资审通过否 | bpchar | 1 |  | √ | '0' | 资审通过否,枚举: 0 :未资审 1 :资审通过 2 :资审不通过 |
| 13 | fisdownload | 是否下载标书 | bpchar | 1 |  | √ | '0' | 是否下载标书 |
| 14 | fenrolllinkman | fenrolllinkman | varchar | 50 |  | √ | ' ' |  |
| 15 | fisdiscard | 是否废标 | bpchar | 1 |  | √ | '0' | 是否废标 |
| 16 | fenrollphone | fenrollphone | varchar | 50 |  | √ | ' ' |  |
| 17 | fenrollremark | fenrollremark | varchar | 255 |  | √ | ' ' |  |
| 18 | fpackageid | 标段名称 | int8 | 64 |  | √ | 0 | 标段名称 src_packagef7 |
| 19 | fsupname | 供应商名称 | varchar | 255 |  | √ | ' ' | 供应商名称 |
| 20 | fpublisherid | 发标人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 21 | fremark | 报名说明 | varchar | 100 |  | √ | ' ' | 报名说明 |
| 22 | fenrolladdress | fenrolladdress | varchar | 100 |  | √ | ' ' |  |
| 23 | fphone | 联系电话 | varchar | 50 |  | √ | ' ' | 联系电话 |
| 24 | fpublishstatus | 发标状态 | bpchar | 1 |  | √ | 'A' | 发标状态,枚举: A :待发标 B :已发标 |
| 25 | fenrollduty | fenrollduty | varchar | 50 |  | √ | ' ' |  |
| 26 | fparentid | 父单据id | varchar | 50 |  | √ | ' ' | 父单据id |
| 27 | friskremark | 风险摘要 | varchar | 510 |  | √ | ' ' | 风险摘要 |
| 28 | femail | 电子邮件 | varchar | 50 |  | √ | ' ' | 电子邮件 |
| 29 | faptitudenote | 资审意见 | varchar | 255 |  | √ | ' ' | 资审意见 |
| 30 | freason | 废标原因 | varchar | 255 |  | √ | ' ' | 废标原因 |
| 31 | fenrollpackageid | fenrollpackageid | int8 | 64 |  | √ | 0 |  |
| 32 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 注册供应商 src_supplier |
| 33 | fduty | 职位 | varchar | 50 |  | √ | ' ' | 职位 |
| 34 | fsuppliertype | 供应商类别 | varchar | 30 |  | √ | ' ' | 供应商类别,枚举: src_supplier :注册供应商 src_supplier_inner :内部供应商(员工) src_supplier_tmp :临时供应商 bd_supplier :供应商 |
| 35 | fenrollnote | fenrollnote | varchar | 255 |  | √ | ' ' |  |
| 36 | fisaptpush2 | 资质后审下达否 | bpchar | 1 |  | √ | '0' | 资质后审下达否 |
| 37 | fsupplierip | 供应商IP | varchar | 100 |  | √ | ' ' | 供应商IP |
| 38 | fenrollsupplierid | fenrollsupplierid | int8 | 64 |  | √ | 0 |  |
| 39 | fpublishdate | 发标日期 | timestamp | 0 |  |  | null | 发标日期 |
| 40 | flinkman | 联系人 | varchar | 50 |  | √ | ' ' | 联系人 |
| 41 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_enrollsupplier_fsup |  | fsupplierid |
| 2 | pk_src_enrollsupplier |  | fentryid |
| 3 | idx_src_enrollsupplier_fepag |  | fenrollpackageid |
| 4 | idx_src_enrollsupplier_fesup |  | fenrollsupplierid |
| 5 | idx_src_enrollsupplier_fpid |  | fparentid |
| 6 | idx_src_enrollsupplier_fid |  | fid |
