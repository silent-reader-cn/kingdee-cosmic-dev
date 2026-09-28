# 工作流指标库-wf_indicatorinfomanage

## 工作流指标库-多语言表 t_wf_indicatorinfomanage_l

- **表名称：** 工作流指标库-多语言表
- **表名：** t_wf_indicatorinfomanage_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |

---

## 工作流指标库-主表 t_wf_indicatorinfomanage

- **表名称：** 工作流指标库-主表
- **表名：** t_wf_indicatorinfomanage

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 3 | fgroup | 分组 | varchar | 50 |  | √ | ' ' | 分组 |
| 4 | fenable | 启用 | bpchar | 1 |  | √ | '0' | 启用 |
| 5 | fnumber | 编码 | varchar | 200 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_indicatorinfo_number |  | fnumber |
| 2 | pk_wf_indicatorinfomanage |  | fid |
