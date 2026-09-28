# 指引工作台-xkguide_workbench

## 指引工作台-主表 t_xkbase_wb_guide

- **表名称：** 指引工作台-主表
- **表名：** t_xkbase_wb_guide

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmaintitle | 主标题 | varchar | 100 |  |  | ' ' | 主标题 |
| 3 | fsubtitle | 副标题 | varchar | 500 |  |  | ' ' | 副标题 |
| 4 | fbizappid | 业务应用 | varchar | 50 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkbase_wb_guide |  | fid |
| 2 | idx_wb_guide_appid |  | fbizappid |

---

## 指引工作台-多语言表 t_xkbase_wb_guide_l

- **表名称：** 指引工作台-多语言表
- **表名：** t_xkbase_wb_guide_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmaintitle | 主标题 | varchar | 500 |  | √ | ' ' | 主标题 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fsubtitle | 副标题 | varchar | 2000 |  | √ | ' ' | 副标题 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkbase_wb_guide_l |  | fpkid |
| 2 | idx_wb_guide_l_fid |  | fid |
