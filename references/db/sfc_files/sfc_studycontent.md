# 学习内容(废弃)-sfc_studycontent

## 人员分录-子表 t_sfc_studyuser

- **表名称：** 人员分录-子表
- **表名：** t_sfc_studyuser

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fuser | 工号 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fprofessiona | 行业 | int8 | 64 |  | √ | 0 | [树形基础资料模板 mpdm_professiona](../mpdm_files/mpdm_professiona.md) |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_studyuser_fk |  | fid |
| 2 | pk_sfc_studyuser |  | fentryid |

---

## 学习内容(废弃)-主表 t_sfc_studycontent

- **表名称：** 学习内容(废弃)-主表
- **表名：** t_sfc_studycontent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 学习标题 | varchar | 50 |  | √ | ' ' | 学习标题 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fstudycontent | 学习内容 | varchar | 2000 |  | √ | ' ' | 学习内容 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fexpdate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 7 | fismust | 必学 | bpchar | 1 |  | √ | '0' | 必学 |
| 8 | fdatasrc | 数据来源 | int8 | 64 |  | √ | 0 | [数据来源(废弃) sfc_datasrc](../sfc_files/sfc_datasrc.md) |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fistest | 需要考试 | bpchar | 1 |  | √ | '0' | 需要考试 |
| 12 | fopenurl | 访问路径 | varchar | 500 |  | √ | ' ' | 访问路径 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 17 | fstudytype | 学习类型 | int8 | 64 |  | √ | 0 | [学习类型(废弃) sfc_studytype](../sfc_files/sfc_studytype.md) |
| 18 | fpublishdate | 发布日期 | timestamp | 0 |  |  | null | 发布日期 |
| 19 | fstudynumber | 学习编号 | varchar | 50 |  | √ | ' ' | 学习编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sfc_studycon_fnumber_idx |  | fnumber |
| 2 | pk_sfc_studycontent |  | fid |

---

## 工卡分录-子表 t_sfc_studycard

- **表名称：** 工卡分录-子表
- **表名：** t_sfc_studycard

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fenginetype | 发动机型号 | varchar | 500 |  | √ | ' ' | 发动机型号 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fworkcard | 工卡编码 | int8 | 64 |  | √ | 0 | [工卡 mpdm_mrocardroute](../mpdm_files/mpdm_mrocardroute.md) |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_studycard_fk |  | fid |
| 2 | pk_sfc_studycard |  | fentryid |

---

## 学习内容(废弃)-多语言表 t_sfc_studycontent_l

- **表名称：** 学习内容(废弃)-多语言表
- **表名：** t_sfc_studycontent_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 学习标题 | varchar | 50 |  | √ | ' ' | 学习标题 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_studycontent_l_0 |  | fid,flocaleid |
| 2 | pk_sfc_studycontent_l |  | fpkid |
