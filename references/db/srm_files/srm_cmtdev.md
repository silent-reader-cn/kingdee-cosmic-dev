# 企业研发工程技术能力-srm_cmtdev

## 企业研发工程技术能力-主表 t_srm_compentdevelop

- **表名称：** 企业研发工程技术能力-主表
- **表名：** t_srm_compentdevelop

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fprojectid | 寻源项目F7 | int8 | 64 |  | √ | 0 | [招标项目F7 src_projectf7](../src_files/src_projectf7.md) |
| 3 | fparentid | 父单据ID | varchar | 100 |  | √ | ' ' | 父单据ID |
| 4 | fclassiccase | 经典案例（请简要说明） | varchar | 255 |  | √ | ' ' | 经典案例（请简要说明） |
| 5 | fentitykey | 组件标识 | varchar | 100 |  | √ | ' ' | 组件标识 |
| 6 | fmainorgid | 主业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fpentitykey | 父单据标识 | varchar | 100 |  | √ | ' ' | 父单据标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_srm_compentdevelop_parent |  | fparentid |
| 2 | pk_t_srm_compentdevelop |  | fid |

---

## 专利/专用技术/许可-子表 t_srm_compdevelopentry

- **表名称：** 专利/专用技术/许可-子表
- **表名：** t_srm_compdevelopentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | forganization | 授予机构 | varchar | 255 |  | √ | ' ' | 授予机构 |
| 3 | fname | 专利/专用技术/许可名称 | varchar | 255 |  | √ | ' ' | 专利/专用技术/许可名称 |
| 4 | fspecial | 特点与价值 | varchar | 255 |  | √ | ' ' | 特点与价值 |
| 5 | fused | 适用于 | varchar | 255 |  | √ | ' ' | 适用于 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fvaliddateto | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_srm_compdevelopentry |  | fentryid |
| 2 | idx_srm_cpdevelopentry_fid |  | fid |
