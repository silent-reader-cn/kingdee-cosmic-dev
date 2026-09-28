# 参与人模型配置-wf_participantmodelconfig

## 参与人模型配置-多语言表 t_wf_participantmodelcfg_l

- **表名称：** 参与人模型配置-多语言表
- **表名：** t_wf_participantmodelcfg_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 184 |  | √ | ' ' | 名称 |
| 3 | fapplicationname | 应用名称 | varchar | 184 |  | √ | ' ' | 应用名称 |
| 4 | flocaleid | flocaleid | varchar | 8 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_wf_participantmodelcfg_l_pkey |  | fpkid |
| 2 | idx_wf_participantcfg_loc |  | fid,flocaleid |

---

## 参与人模型配置-主表 t_wf_participantmodelcfg

- **表名称：** 参与人模型配置-主表
- **表名：** t_wf_participantmodelcfg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | fname | varchar | 184 |  | √ | ' ' |  |
| 3 | favatar | 图片路径 | varchar | 300 |  | √ | ' ' | 图片路径 |
| 4 | ftype | 类型 | varchar | 30 |  | √ | ' ' | 类型 |
| 5 | fparser | 解析器 | varchar | 255 |  | √ | ' ' | 解析器 |
| 6 | fapplicationid | 应用id | varchar | 36 |  | √ | ' ' | 应用id |
| 7 | fapplicationname | fapplicationname | varchar | 184 |  | √ | ' ' |  |
| 8 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 9 | fformid | 表单id | varchar | 255 |  | √ | ' ' | 表单id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_participantmodelcfg |  | fapplicationid |
| 2 | t_wf_participantmodelcfg_pkey |  | fid |
