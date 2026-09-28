# 供应商投标文件-src_biddoc_tnd

## 标书文件分录-子表 t_src_biddocentry

- **表名称：** 标书文件分录-子表
- **表名：** t_src_biddocentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcentryid | fsrcentryid | varchar | 50 |  | √ | ' ' |  |
| 3 | fentrystatus | 状态 | bpchar | 1 |  | √ | ' ' | 状态,枚举: A :待投标 B :已投标 C :已开标 D :已关闭 E :已定标 F :已签约 G :暂存 H :已弃标 I :已废标 J :已终止 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 6 | fsuppliercode | fsuppliercode | varchar | 50 |  | √ | ' ' |  |
| 7 | fbilldate | fbilldate | timestamp | 0 |  |  | null |  |
| 8 | fpurlistid | fpurlistid | int8 | 64 |  | √ | 0 |  |
| 9 | fisaptitude | 资审结果 | bpchar | 1 |  | √ | '0' | 资审结果,枚举: 0 :未资审 1 :资审合格 2 :资审不合格 |
| 10 | fisneedbiddoc | 供方必须上传标书 | bpchar | 1 |  | √ | '0' | 供方必须上传标书 |
| 11 | ffileclass | 文件分类 | varchar | 100 |  | √ | ' ' | 文件分类 |
| 12 | ffilename | 文件名称 | varchar | 2000 |  |  | ' ' | 文件名称 |
| 13 | fcompkey | 组件标识 | varchar | 50 |  | √ | ' ' | 组件标识 |
| 14 | fpackageid | 标段 | int8 | 64 |  | √ | 0 | 标段名称 src_packagef7 |
| 15 | fturns | fturns | varchar | 2 |  | √ | ' ' |  |
| 16 | fprojectid | 招标项目 | int8 | 64 |  | √ | 0 | 招标项目F7 src_projectf7 |
| 17 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 18 | fsrcbillid | 源单ID | varchar | 50 |  | √ | ' ' | 源单ID |
| 19 | ffiletype | 文件类型 | bpchar | 1 |  | √ | ' ' | 文件类型,枚举: 1 :技术标书 2 :商务标书 3 :通用标书 4 :商务综合标书 5 :资质审查标书 6 :报名附件 7 :协同附件 |
| 20 | fsrcentryid2 | 源单分录ID | int8 | 64 |  | √ | 0 | 源单分录ID |
| 21 | faptitudenote | 资审意见 | varchar | 255 |  | √ | ' ' | 资审意见 |
| 22 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 注册供应商 src_supplier |
| 23 | fsuppliertype | 供应商类别 | varchar | 30 |  | √ | ' ' | 供应商类别,枚举: src_supplier :注册供应商 src_supplier_inner :内部供应商(员工) src_supplier_tmp :临时供应商 bd_supplier :供应商 |
| 24 | fsupplierip | fsupplierip | varchar | 100 |  | √ | ' ' |  |
| 25 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 26 | ffilereq | 文件要求 | varchar | 255 |  | √ | ' ' | 文件要求 |
| 27 | fbilltype | 单据类型 | bpchar | 1 |  | √ | ' ' | 单据类型,枚举: 1 :标书编制 2 :标书上传 3 :投标报名 4 :竞价大厅 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_biddocentry_fid |  | fid |
| 2 | pk_src_biddocentry |  | fentryid |
| 3 | idx_src_biddocentry_packid |  | fpackageid |
| 4 | idx_src_biddocentry_proid |  | fprojectid |
| 5 | idx_src_biddocentry_ppurid |  | fpurlistid |
| 6 | idx_src_biddocentry_supid |  | fsupplierid |

---

## 供应商投标文件-主表 t_src_biddoc

- **表名称：** 供应商投标文件-主表
- **表名：** t_src_biddoc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forigin | 发起方 | varchar | 30 |  | √ | ' ' | 发起方,枚举: 1 :采购方端 2 :供应商端 3 :两端公用 |
| 3 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 4 | fbillstatus | fbillstatus | bpchar | 1 |  | √ | ' ' |  |
| 5 | fbizstatus | fbizstatus | bpchar | 1 |  | √ | ' ' |  |
| 6 | fentitykey | 组件标识 | varchar | 50 |  | √ | ' ' | 组件标识 |
| 7 | fisquickpur | fisquickpur | bpchar | 1 |  | √ | '0' |  |
| 8 | fmanagetype | fmanagetype | bpchar | 1 |  | √ | ' ' |  |
| 9 | fbillno | fbillno | varchar | 30 |  | √ | ' ' |  |
| 10 | fpentitykey | 父单据标识 | varchar | 50 |  | √ | ' ' | 父单据标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_biddoc_fentitykey |  | fentitykey |
| 2 | idx_src_biddoc_fparentid |  | fparentid |
| 3 | pk_src_biddoc |  | fid |
| 4 | idx_src_biddoc_fbillno |  | fbillno |

---

## 文件附件-附件表 t_src_biddocentry_fj

- **表名称：** 文件附件-附件表
- **表名：** t_src_biddocentry_fj

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
| 1 | pk_src_biddocentry_fj |  | fpkid |
| 2 | idx_src_biddocentry_bid |  | fbasedataid |
| 3 | idx_src_biddocentry_fj |  | fentryid |
