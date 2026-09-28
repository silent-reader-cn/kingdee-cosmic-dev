# 招聘消息模板-recru_msgtemplate

## 招聘消息模板-多语言表 t_recru_msgtemplate_l

- **表名称：** 招聘消息模板-多语言表
- **表名：** t_recru_msgtemplate_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 模板名称 | varchar | 100 |  | √ | ' ' | 模板名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_recru_msgtemplate_l |  | fpkid |
| 2 | idx_msgtemplate_l |  | fid |

---

## 招聘消息模板-主表 t_recru_msgtemplate

- **表名称：** 招聘消息模板-主表
- **表名：** t_recru_msgtemplate

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 模板名称 | varchar | 50 |  | √ | ' ' | 模板名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | femailtheme | 邮件主题 | varchar | 50 |  | √ | ' ' | 邮件主题 |
| 6 | femailrichtextfd | 邮件内容 | varchar | 50 |  | √ | ' ' | 邮件内容 |
| 7 | femailrichtextfd_tag | 邮件内容_详情 | text | 0 |  |  | null | 邮件内容_详情 |
| 8 | fnotifymethodid | 通知方式 | int8 | 64 |  | √ | 0 | [招聘消息通知方式 recru_notifymethod](../recru_files/recru_notifymethod.md) |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | varchar | 2 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fenable | 使用状态 | varchar | 2 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fpushsceneid | 推送场景 | int8 | 64 |  | √ | 0 | [招聘消息推送场景 recru_msgpushscene](../recru_files/recru_msgpushscene.md) |
| 15 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 16 | fissyspreset | 系统预置 | varchar | 2 |  | √ | ' ' | 系统预置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msgtemplate |  | fname,fnumber |
| 2 | pk_recru_msgtemplate |  | fid |
