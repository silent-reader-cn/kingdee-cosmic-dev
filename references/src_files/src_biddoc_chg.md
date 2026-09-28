# 招标文件变更-src_biddoc_chg

## 变更前文件附件-附件表 t_src_biddocentry_fj

- **表名称：** 变更前文件附件-附件表
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

---

## 标书文件分录-子表 t_src_biddocentry_chg

- **表名称：** 标书文件分录-子表
- **表名：** t_src_biddocentry_chg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcentryid | fsrcentryid | varchar | 50 |  | √ | ' ' |  |
| 3 | fprojectid | 招标项目 | int8 | 64 |  | √ | 0 | 招标项目F7 src_projectf7 |
| 4 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 5 | fsrcbillid | 源单ID | varchar | 50 |  | √ | ' ' | 源单ID |
| 6 | ffiletype | 文件类型 | bpchar | 1 |  | √ | ' ' | 文件类型,枚举: 1 :技术标书 2 :商务标书 3 :通用标书 4 :商务综合标书 5 :资质审查标书 6 :报名附件 7 :协同附件 |
| 7 | fentrystatus | 状态 | bpchar | 1 |  | √ | ' ' | 状态,枚举: A :待投标 B :已投标 C :已开标 D :已关闭 E :已定标 F :已签约 G :暂存 H :已弃标 I :已废标 J :已终止 |
| 8 | fsrcentryid2 | 源单分录ID | int8 | 64 |  | √ | 0 | 源单分录ID |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | fnote | 变更前文件说明 | varchar | 255 |  | √ | ' ' | 变更前文件说明 |
| 11 | faptitudenote | 资审意见 | varchar | 255 |  | √ | ' ' | 资审意见 |
| 12 | fsuppliercode | fsuppliercode | varchar | 50 |  | √ | ' ' |  |
| 13 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 注册供应商 src_supplier |
| 14 | fisaptitude | 资审结果 | bpchar | 1 |  | √ | '0' | 资审结果,枚举: 0 :未资审 1 :资审合格 2 :资审不合格 |
| 15 | fsuppliertype | 供应商类别 | varchar | 30 |  | √ | ' ' | 供应商类别,枚举: src_supplier :注册供应商 src_supplier_inner :内部供应商(员工) src_supplier_tmp :临时供应商 bd_supplier :供应商 |
| 16 | fpackfilename_new | 变更后文件名称 | varchar | 512 |  | √ | ' ' | 变更后文件名称 |
| 17 | fisneedbiddoc | 供方必须上传标书 | bpchar | 1 |  | √ | '0' | 供方必须上传标书 |
| 18 | ffileclass | 文件分类 | varchar | 100 |  | √ | ' ' | 文件分类 |
| 19 | ffilename | 变更前文件名称 | varchar | 2000 |  |  | ' ' | 变更前文件名称 |
| 20 | fcompkey | 组件标识 | varchar | 50 |  | √ | ' ' | 组件标识 |
| 21 | fpackageid | 标段 | int8 | 64 |  | √ | 0 | 标段名称 src_packagef7 |
| 22 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 23 | ffilereq | ffilereq | varchar | 255 |  | √ | ' ' |  |
| 24 | fbilltype | 单据类型 | bpchar | 1 |  | √ | ' ' | 单据类型,枚举: 1 :标书编制 2 :标书上传 3 :投标报名 4 :竞价大厅 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_biddocentry_chg |  | fentryid |
| 2 | idx_src_biddocentry_chg_fid |  | fid |

---

## 招标文件变更-主表 t_src_biddoc_chg

- **表名称：** 招标文件变更-主表
- **表名：** t_src_biddoc_chg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fprojectid | 寻源项目F7 | int8 | 64 |  | √ | 0 | 招标项目F7 src_projectf7 |
| 3 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | forgid | 主业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fbizstatus | fbizstatus | bpchar | 1 |  | √ | ' ' |  |
| 7 | fentitykey | 组件标识 | varchar | 50 |  | √ | ' ' | 组件标识 |
| 8 | fpentitykey | 父单据标识 | varchar | 50 |  | √ | ' ' | 父单据标识 |
| 9 | forigin | 发起方 | varchar | 30 |  | √ | ' ' | 发起方,枚举: 1 :采购方端 2 :供应商端 3 :两端公用 |
| 10 | fbidchangeid | 寻源项目变更F7 | int8 | 64 |  | √ | 0 | 寻源项目变更F7 src_bidchangef7 |
| 11 | fchgsrcbillid | 变更源单ID | int8 | 64 |  | √ | 0 | 变更源单ID |
| 12 | fisquickpur | fisquickpur | bpchar | 1 |  | √ | '0' |  |
| 13 | fmanagetype | fmanagetype | bpchar | 1 |  | √ | ' ' |  |
| 14 | fcompbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 15 | fbillno | fbillno | varchar | 30 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_biddoc_chg_fbillno |  | fbillno |
| 2 | idx_src_biddoc_chg_fentitykey |  | fentitykey |
| 3 | idx_src_biddoc_chg_fparentid |  | fparentid |
| 4 | pk_src_biddoc_chg |  | fid |

---

## 变更后文件附件-附件表 t_src_biddocentry_chg_fj

- **表名称：** 变更后文件附件-附件表
- **表名：** t_src_biddocentry_chg_fj

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
| 1 | idx_src_biddocentry_chg_fj_eid |  | fentryid |
| 2 | idx_src_biddocentry_chg_fj_bid |  | fbasedataid |
| 3 | pk_src_biddocentry_chg_fj |  | fpkid |
