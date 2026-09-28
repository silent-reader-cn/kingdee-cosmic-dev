# 代理资审回复-tnd_aptitude_pur

## 供应商用户-多选基础资料表 t_src_supplieruser

- **表名称：** 供应商用户-多选基础资料表
- **表名：** t_src_supplieruser

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [供应商用户 pur_supuser](../basedata_files/pur_supuser.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_supplieruser_bid |  | fbasedataid |
| 2 | pk_src_supplieruser |  | fpkid |
| 3 | idx_src_supplieruser_fid |  | fid |

---

## 供应商资审文件-附件表 t_src_supaptattach

- **表名称：** 供应商资审文件-附件表
- **表名：** t_src_supaptattach

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [附件字段实体 bd_attachment](../frame_files/bd_attachment.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_supaptattach_bid |  | fbasedataid |
| 2 | pk_src_supaptattach |  | fpkid |

---

## 采购方资审文件-附件表 t_src_puraptattach

- **表名称：** 采购方资审文件-附件表
- **表名：** t_src_puraptattach

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [附件字段实体 bd_attachment](../frame_files/bd_attachment.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_puraptattach_fbid |  | fbasedataid |
| 2 | pk_src_puraptattach |  | fpkid |

---

## 代理资审回复-主表 t_src_score

- **表名称：** 代理资审回复-主表
- **表名：** t_src_score

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsrcentryid | fsrcentryid | int8 | 64 |  | √ | 0 |  |
| 3 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fbasetype | 基本类型 | bpchar | 1 |  | √ | '1' | 基本类型,枚举: 1 :技术类 2 :商务类 3 :商务综合类 4 :资质审查类 5 :供应商分析类 6 :综合评标类 7 :资质后审类 |
| 5 | fbizstatus | fbizstatus | bpchar | 1 |  | √ | ' ' |  |
| 6 | fschemeid | 资审方案 | int8 | 64 |  | √ | 0 | [方案配置 src_scheme](../src_files/src_scheme.md) |
| 7 | fbilldate | fbilldate | timestamp | 0 |  |  | null |  |
| 8 | fsuppliercode | fsuppliercode | varchar | 50 |  | √ | ' ' |  |
| 9 | fpurlistid | fpurlistid | int8 | 64 |  | √ | 0 |  |
| 10 | fisaptitude | 是否资质审查 | bpchar | 1 |  | √ | '0' | 是否资质审查 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fscoretype | fscoretype | bpchar | 1 |  | √ | ' ' |  |
| 13 | faptituderesult | 资审结果 | bpchar | 1 |  | √ | '0' | 资审结果,枚举: 0 :未资审 1 :资审合格 2 :资审不合格 |
| 14 | fcreatorid | 项目创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fpackageid | 标段名称 | int8 | 64 |  | √ | 0 | [标段名称 src_packagef7](../src_files/src_packagef7.md) |
| 16 | fbillno | 资审单号 | varchar | 30 |  | √ | ' ' | 资审单号 |
| 17 | fispuraptitude | 是否代理资审回复 | bpchar | 1 |  | √ | '0' | 是否代理资审回复 |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fisaptitude2 | fisaptitude2 | bpchar | 1 |  | √ | '0' |  |
| 20 | fprojectid | 寻源项目 | int8 | 64 |  | √ | 0 | [招标项目F7 src_projectf7](../src_files/src_projectf7.md) |
| 21 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | fagents | 代理评委 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fsumscore | fsumscore | numeric | 23 | 10 | √ | 0 |  |
| 25 | faptitudenote | 资审意见 | varchar | 255 |  | √ | ' ' | 资审意见 |
| 26 | fauditdate | 回复时间 | timestamp | 0 |  |  | null | 回复时间 |
| 27 | fdescription | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 28 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 29 | ffinishdate | ffinishdate | timestamp | 0 |  |  | null |  |
| 30 | forigncreator | forigncreator | int8 | 64 |  | √ | 0 |  |
| 31 | findextypeid | 资审类型 | int8 | 64 |  | √ | 0 | [指标类型 src_indexclass](../src_files/src_indexclass.md) |
| 32 | fcfmstatus | 回复状态 | bpchar | 1 |  | √ | 'A' | 回复状态,枚举: A :待回复 B :已提交 C :已回复 |
| 33 | fsuppliertype | fsuppliertype | varchar | 30 |  | √ | ' ' |  |
| 34 | fminvalue | fminvalue | numeric | 23 | 10 | √ | 0 |  |
| 35 | fisaptitudereply | 是否需要资审协同 | bpchar | 1 |  | √ | '0' | 是否需要资审协同 |
| 36 | fbillindexscore | fbillindexscore | numeric | 23 | 10 | √ | 0 |  |
| 37 | finputscore | finputscore | numeric | 23 | 10 | √ | 0 |  |
| 38 | fbizstatus2 | fbizstatus2 | bpchar | 1 |  | √ | ' ' |  |
| 39 | fsupplierip | 供应商IP | varchar | 100 |  | √ | ' ' | 供应商IP |
| 40 | fcfmstatus_sup | 供应商回复状态 | bpchar | 1 |  | √ | 'A' | 供应商回复状态,枚举: A :待回复 B :已提交 C :已回复 |
| 41 | fcfmstatus_pur | 采购方回复状态 | bpchar | 1 |  | √ | 'A' | 采购方回复状态,枚举: A :待回复 B :已提交 C :已回复 |
| 42 | fisvalid | fisvalid | bpchar | 1 |  | √ | '0' |  |
| 43 | fauditorid | 回复人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_score_packageid |  | fpackageid |
| 2 | idx_src_score_fbillno |  | fbillno |
| 3 | idx_src_score_supid |  | fsupplierid |
| 4 | idx_src_score_projectid |  | fprojectid |
| 5 | pk_src_score |  | fid |

---

## 评委-多选基础资料表 t_src_assessscorer2

- **表名称：** 评委-多选基础资料表
- **表名：** t_src_assessscorer2

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
| 1 | pk_src_assessscorer2 |  | fpkid |
| 2 | idx_src_assessscorer2_fid |  | fid |
| 3 | idx_src_assessscorer2_bid |  | fbasedataid |
