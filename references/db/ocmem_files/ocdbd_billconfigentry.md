# 单据配置分录-ocdbd_billconfigentry

## 单据配置分录-主表 t_ocdbd_bconfigentry

- **表名称：** 单据配置分录-主表
- **表名：** t_ocdbd_bconfigentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fisdisplay | 显示 | bpchar | 1 |  | √ | '0' | 显示 |
| 3 | fisrequired | 必录 | bpchar | 1 |  | √ | '0' | 必录 |
| 4 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 5 | ffieldnameid | ffieldnameid | int8 | 64 |  | √ | 0 |  |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_bconfigentry |  | fentryid |
| 2 | idx_ocdbd_bconfigentry_fid |  | fid |

---

## 单据配置分录-多语言表 t_ocdbd_bconfigentry_l

- **表名称：** 单据配置分录-多语言表
- **表名：** t_ocdbd_bconfigentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
