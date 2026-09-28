# 招聘快捷推荐-recru_recommend

## 招聘快捷推荐-主表 t_recru_recommend

- **表名称：** 招聘快捷推荐-主表
- **表名：** t_recru_recommend

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 推荐名称 | varchar | 50 |  | √ | ' ' | 推荐名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fstatus | 数据状态 | varchar | 3 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | faichat | 是否与AI对话 | bpchar | 1 |  | √ | '0' | 是否与AI对话 |
| 8 | frecommendkey | 推荐标识 | varchar | 50 |  | √ | ' ' | 推荐标识 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fuserinput | 是否作为用户输入 | bpchar | 1 |  | √ | '0' | 是否作为用户输入 |
| 12 | fnodeid | 任务节点 | int8 | 64 |  | √ | 0 | [任务节点编排 recru_agenttask](../recru_files/recru_agenttask.md) |
| 13 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | furl | 调用url | varchar | 200 |  | √ | ' ' | 调用url |
| 15 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_recru_recommend |  | fid |
| 2 | idx_recru_recommend_node |  | fnodeid |

---

## 招聘快捷推荐-多语言表 t_recru_recommend_l

- **表名称：** 招聘快捷推荐-多语言表
- **表名：** t_recru_recommend_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 推荐名称 | varchar | 50 |  | √ | ' ' | 推荐名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_recru_recommend_l |  | fpkid |
| 2 | idx_recru_recommend_l |  | fid,flocaleid |
