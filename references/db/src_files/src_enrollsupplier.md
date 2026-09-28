# 报名供应商(后台元数据)-src_enrollsupplier

## 关联标的(发标)-多选基础资料表 t_src_invitesupplier_item

- **表名称：** 关联标的(发标)-多选基础资料表
- **表名：** t_src_invitesupplier_item

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 采购清单F7 src_purlistf7 |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_invitesup_item_bid |  | fbasedataid |
| 2 | idx_src_invitesup_item_eid |  | fentryid |
| 3 | pk_src_invitesupplier_item |  | fpkid |

---

## 关联标的(范围)-多选基础资料表 t_src_invitesupplierscope

- **表名称：** 关联标的(范围)-多选基础资料表
- **表名：** t_src_invitesupplierscope

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 采购清单F7 src_purlistf7 |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_invitesupplierscope |  | fpkid |
| 2 | idx_src_invitesupscope_bid |  | fbasedataid |
| 3 | idx_src_invitesupscope_eid |  | fentryid |

---

## 附件-附件表 t_src_enrollsupplier_fj

- **表名称：** 附件-附件表
- **表名：** t_src_enrollsupplier_fj

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [附件字段实体 bd_attachment](../frame_files/bd_attachment.md) |
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
| 5 | fisexemptapt | 免资审 | bpchar | 1 |  | √ | '0' | 免资审 |
| 6 | fsocietycreditcode | 统一社会信用代码 | varchar | 255 |  | √ | ' ' | 统一社会信用代码 |
| 7 | fisbidpush | 评标任务下达否 | bpchar | 1 |  | √ | '0' | 评标任务下达否 |
| 8 | fisselect | 是否推荐 | bpchar | 1 |  | √ | '0' | 是否推荐 |
| 9 | fseq | 序号 | int8 | 64 |  | √ | 0 | 序号 |
| 10 | fnote | 推荐原因说明 | varchar | 100 |  | √ | ' ' | 推荐原因说明 |
| 11 | fenrollemail | fenrollemail | varchar | 50 |  | √ | ' ' |  |
| 12 | fapplytime | 报名时间 | timestamp | 0 |  |  | null | 报名时间 |
| 13 | fisaptitude | 资审通过否 | bpchar | 1 |  | √ | '0' | 资审通过否,枚举: 0 :未资审 1 :资审通过 2 :资审不通过 |
| 14 | fisdownload | 是否下载标书 | bpchar | 1 |  | √ | '0' | 是否下载标书 |
| 15 | fenrolllinkman | fenrolllinkman | varchar | 50 |  | √ | ' ' |  |
| 16 | fisdiscard | 是否废标 | bpchar | 1 |  | √ | '0' | 是否废标 |
| 17 | fenrollphone | fenrollphone | varchar | 50 |  | √ | ' ' |  |
| 18 | fenrollremark | fenrollremark | varchar | 255 |  | √ | ' ' |  |
| 19 | fpurlistnote | 关联标的 | varchar | 50 |  | √ | ' ' | 关联标的 |
| 20 | fpackageid | 标段名称 | int8 | 64 |  | √ | 0 | [标段名称 src_packagef7](../src_files/src_packagef7.md) |
| 21 | fsupname | 供应商名称 | varchar | 255 |  | √ | ' ' | 供应商名称 |
| 22 | fpublisherid | 发标人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | fremark | 报名说明 | varchar | 100 |  | √ | ' ' | 报名说明 |
| 24 | fenrolladdress | fenrolladdress | varchar | 100 |  | √ | ' ' |  |
| 25 | fphone | 联系电话 | varchar | 50 |  | √ | ' ' | 联系电话 |
| 26 | fpublishstatus | 发标状态 | bpchar | 1 |  | √ | 'A' | 发标状态,枚举: A :待发标 B :已发标 |
| 27 | fenrollduty | fenrollduty | varchar | 50 |  | √ | ' ' |  |
| 28 | fparentid | 父单据id | varchar | 50 |  | √ | ' ' | 父单据id |
| 29 | friskremark | 风险摘要 | varchar | 510 |  | √ | ' ' | 风险摘要 |
| 30 | femail | 电子邮件 | varchar | 50 |  | √ | ' ' | 电子邮件 |
| 31 | faptitudenote | 资审意见 | varchar | 255 |  | √ | ' ' | 资审意见 |
| 32 | freason | 废标原因 | varchar | 255 |  | √ | ' ' | 废标原因 |
| 33 | fenrollpackageid | fenrollpackageid | int8 | 64 |  | √ | 0 |  |
| 34 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 注册供应商 src_supplier |
| 35 | fduty | 职位 | varchar | 50 |  | √ | ' ' | 职位 |
| 36 | fsuppliertype | 供应商类别 | varchar | 30 |  | √ | ' ' | 供应商类别,枚举: src_supplier :注册供应商 src_supplier_inner :内部供应商(员工) src_supplier_tmp :临时供应商 bd_supplier :供应商 |
| 37 | fisaptitudereply | 资审回复否 | bpchar | 1 |  | √ | '0' | 资审回复否 |
| 38 | fenrollnote | fenrollnote | varchar | 255 |  | √ | ' ' |  |
| 39 | fisaptpush2 | 资质后审下达否 | bpchar | 1 |  | √ | '0' | 资质后审下达否 |
| 40 | fsupplierip | 供应商IP | varchar | 100 |  | √ | ' ' | 供应商IP |
| 41 | fenrollsupplierid | fenrollsupplierid | int8 | 64 |  | √ | 0 |  |
| 42 | fpublishdate | 发标日期 | timestamp | 0 |  |  | null | 发标日期 |
| 43 | flinkman | 联系人 | varchar | 50 |  | √ | ' ' | 联系人 |
| 44 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

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
