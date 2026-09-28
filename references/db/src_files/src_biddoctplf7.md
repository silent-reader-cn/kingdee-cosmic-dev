# 标书文件F7-src_biddoctplf7

## 标书文件F7-主表 t_src_biddocentry

- **表名称：** 标书文件F7-主表
- **表名：** t_src_biddocentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 2 | fsrcentryid | fsrcentryid | varchar | 50 |  | √ | ' ' |  |
| 3 | fentrystatus | 业务状态 | bpchar | 1 |  | √ | ' ' | 业务状态,枚举: A :待投标 B :已投标 C :已开标 D :已关闭 E :已定标 F :已签约 |
| 4 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 5 | fnote | 文件说明 | varchar | 255 |  | √ | ' ' | 文件说明 |
| 6 | fsuppliercode | 供应商代码 | varchar | 50 |  | √ | ' ' | 供应商代码 |
| 7 | fbilldate | 投标时间 | timestamp | 0 |  |  | null | 投标时间 |
| 8 | fpurlistid | 标的 | int8 | 64 |  | √ | 0 | 采购清单F7 src_purlistf7 |
| 9 | fisaptitude | 资审结果 | bpchar | 1 |  | √ | '0' | 资审结果,枚举: 0 :未资审 1 :资审合格 2 :资审不合格 |
| 10 | fisneedbiddoc | 供方必须上传标书 | bpchar | 1 |  | √ | '0' | 供方必须上传标书 |
| 11 | ffileclass | 文件分类 | varchar | 100 |  | √ | ' ' | 文件分类 |
| 12 | ffilename | 文件名称 | varchar | 2000 |  |  | ' ' | 文件名称 |
| 13 | fcompkey | 组件标识 | varchar | 50 |  | √ | ' ' | 组件标识 |
| 14 | fpackageid | 标段 | int8 | 64 |  | √ | 0 | 标段名称 src_packagef7 |
| 15 | fturns | 议价轮次 | varchar | 2 |  | √ | ' ' | 议价轮次,枚举: |
| 16 | fprojectid | 招标项目 | int8 | 64 |  | √ | 0 | 招标项目F7 src_projectf7 |
| 17 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 18 | fsrcbillid | 源单ID | varchar | 50 |  | √ | ' ' | 源单ID |
| 19 | ffiletype | 文件类型 | bpchar | 1 |  | √ | ' ' | 文件类型,枚举: 1 :技术标书 2 :商务标书 3 :通用标书 4 :商务综合标书 5 :资审审查标书 6 :报名附件 7 :协同附件 |
| 20 | fsrcentryid2 | 源单分录ID | int8 | 64 |  | √ | 0 | 源单分录ID |
| 21 | faptitudenote | 资审意见 | varchar | 255 |  | √ | ' ' | 资审意见 |
| 22 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 注册供应商 src_supplier |
| 23 | fsuppliertype | 供应商类别 | varchar | 30 |  | √ | ' ' | 供应商类别,枚举: src_supplier :注册供应商 src_supplier_inner :内部供应商(员工) src_supplier_tmp :临时供应商 bd_supplier :供应商 |
| 24 | fsupplierip | 供应商IP | varchar | 100 |  | √ | ' ' | 供应商IP |
| 25 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 26 | ffilereq | ffilereq | varchar | 255 |  | √ | ' ' |  |
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
