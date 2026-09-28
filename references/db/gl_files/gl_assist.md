# 核算项目组合-gl_assist

## 核算项目组合-主表 t_gl_assist

- **表名称：** 核算项目组合-主表
- **表名：** t_gl_assist

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fvalue | 核算项目 | varchar | 512 |  | √ | ' ' | 核算项目 |
| 3 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_t_gl_assist |  | fvalue |
| 2 | t_gl_assist_pkey |  | fid |

---

## 核算项目组合纵表(基础资料)-子表 t_gl_assist_bd

- **表名称：** 核算项目组合纵表(基础资料)-子表
- **表名：** t_gl_assist_bd

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fvalue | 核算项目值 | int8 | 64 |  | √ | 0 | 核算项目值 |
| 3 | fflexfield | 核算项目类型 | varchar | 30 |  | √ | ' ' | 核算项目类型 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_assistdb |  | fflexfield,fvalue,fid |
| 2 | idx_gl_assistdb_fid |  | fid |
| 3 | t_gl_assist_bd_pkey |  | fentryid |
| 4 | idx_gl_assistvalue |  | fvalue |

---

## 核算项目组合纵表(文本)-子表 t_gl_assist_txt

- **表名称：** 核算项目组合纵表(文本)-子表
- **表名：** t_gl_assist_txt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fvalue | 核算项目类型 | varchar | 300 |  | √ | ' ' | 核算项目类型 |
| 3 | fflexfield | 核算项目类型 | varchar | 30 |  | √ | ' ' | 核算项目类型 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_assisttxthg |  | fid |
| 2 | idx_gl_assist_txt_fvalue |  | fvalue |
| 3 | t_gl_assist_txt_pkey |  | fentryid |
