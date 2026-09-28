# 指引步骤-xkguide_step

## 指引步骤-多语言表 t_xkbase_guide_step_l

- **表名称：** 指引步骤-多语言表
- **表名：** t_xkbase_guide_step_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbtndonetext | 按钮已完成状态文本 | varchar | 100 |  | √ | ' ' | 按钮已完成状态文本 |
| 3 | fbtninittext | 按钮初始状态文本 | varchar | 100 |  | √ | ' ' | 按钮初始状态文本 |
| 4 | fbtndoingtext | 按钮进行中状态文本 | varchar | 100 |  | √ | ' ' | 按钮进行中状态文本 |
| 5 | fdurationunit | 时长单位 | varchar | 50 |  | √ | ' ' | 时长单位 |
| 6 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 7 | fdesc | 步骤描述 | varchar | 2000 |  | √ | ' ' | 步骤描述 |
| 8 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_step_l_fid |  | fid |
| 2 | pk_t_xkbase_guide_step_l |  | fpkid |

---

## 指引步骤-主表 t_xkbase_guide_step

- **表名称：** 指引步骤-主表
- **表名：** t_xkbase_guide_step

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbtndonetext | 按钮已完成状态文本 | varchar | 20 |  | √ | ' ' | 按钮已完成状态文本 |
| 3 | fbtninittext | 按钮初始状态文本 | varchar | 20 |  | √ | ' ' | 按钮初始状态文本 |
| 4 | findex | 顺序 | int4 | 32 |  | √ | 0 | 顺序 |
| 5 | fdescstyle | 描述样式（json） | text | 0 |  |  | ' ' | 描述样式（json） |
| 6 | fbtndoingtext | 按钮进行中状态文本 | varchar | 20 |  | √ | ' ' | 按钮进行中状态文本 |
| 7 | fdurationstyle | 时长样式（json） | text | 0 |  |  | ' ' | 时长样式（json） |
| 8 | fbizappid | 业务应用 | varchar | 50 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 9 | fbtnstyle | 按钮样式（json） | text | 0 |  |  | ' ' | 按钮样式（json） |
| 10 | fduration | 时长 | int4 | 32 |  | √ | 0 | 时长 |
| 11 | fdurationunit | 时长单位 | varchar | 10 |  | √ | ' ' | 时长单位 |
| 12 | fdesc | 步骤描述 | varchar | 500 |  | √ | ' ' | 步骤描述 |
| 13 | fscope | 查询范围 | varchar | 10 |  | √ | '0' | 查询范围,枚举: 0 :多组织/单组织可查 1 :单组织可查 2 :多组织可查 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_step_findex |  | findex |
| 2 | pk_t_xkbase_guide_step |  | fid |
| 3 | idx_step_fbizappid |  | fbizappid |
