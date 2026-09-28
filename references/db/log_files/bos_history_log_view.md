# 历史记录-bos_history_log_view

## 历史记录-多语言表 t_log_app_l

- **表名称：** 历史记录-多语言表
- **表名：** t_log_app_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | null |  |
| 2 | fopname | 操作名称 | varchar | 255 |  | √ | null | 操作名称 |
| 3 | fopdescription | 操作描述 | varchar | 255 |  |  | null | 操作描述 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | null | localeid |
| 5 | fclientname | 客户端名称 | varchar | 255 |  |  | null | 客户端名称 |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_log_app_l_opdesc |  | fopdescription |
| 2 | idx_log_app_l_fid |  | fid,flocaleid |
| 3 | t_log_app_l_pkey |  | fpkid |

---

## 历史记录-主表 t_log_app

- **表名称：** 历史记录-主表
- **表名：** t_log_app

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | null | id |
| 2 | fmodifybillid | 数据更新源单内码 | varchar | 36 |  | √ | ' ' | 数据更新源单内码 |
| 3 | fbizobjname | 操作对象名 | varchar | 255 |  | √ | ' ' | 操作对象名 |
| 4 | forgid | 操作组织 | int8 | 64 |  |  | null | 业务单元 bos_org |
| 5 | fclienttype | 客户端类型 | varchar | 30 |  |  | null | 客户端类型,枚举: web :PC端 mobile :移动端 api :接口 |
| 6 | fbizappname | 应用名 | varchar | 255 |  | √ | ' ' | 应用名 |
| 7 | fopdescription | fopdescription | varchar | 255 |  | √ | ' ' |  |
| 8 | fuserid | 操作人 | int8 | 64 |  |  | null | 人员 bos_user |
| 9 | fmodifybillno | 数据更新源单编码 | varchar | 255 |  | √ | ' ' | 数据更新源单编码 |
| 10 | fmodifycontent_tag | 数据更新内容_详情 | text | 0 |  |  | null | 数据更新内容_详情 |
| 11 | fmodifyfields | 数据更新字段 | varchar | 1020 |  | √ | ' ' | 数据更新字段 |
| 12 | farchivetime | 归档时间 | timestamp | 0 |  |  | null | 归档时间 |
| 13 | fbizappid | 应用 | varchar | 36 |  |  | null | 业务应用实体 bos_devportal_bizapp |
| 14 | fclientip | 客户端地址 | varchar | 128 |  |  | null | 客户端地址 |
| 15 | fusername | 操作用户名 | varchar | 255 |  | √ | ' ' | 操作用户名 |
| 16 | fopname | fopname | varchar | 255 |  | √ | ' ' |  |
| 17 | fclientnamee | 客户端名称名 | varchar | 255 |  | √ | ' ' | 客户端名称名 |
| 18 | foptime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 19 | fmodifycontent | 数据更新内容 | varchar | 510 |  |  | null | 数据更新内容 |
| 20 | fopdescriptione | 操作描述名 | varchar | 255 |  | √ | ' ' | 操作描述名 |
| 21 | fopnamee | 操作名称名 | varchar | 255 |  | √ | ' ' | 操作名称名 |
| 22 | fbizobjid | 操作对象 | varchar | 36 |  |  | null | 业务对象 bos_objecttype |
| 23 | forgname | 操作组织名 | varchar | 255 |  | √ | ' ' | 操作组织名 |
| 24 | fclientname | fclientname | varchar | 255 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | ix_log_app_modifybillid |  | fmodifybillid |
| 2 | ix_log_app_userid |  | fuserid |
| 3 | ix_log_app_optimeappuser |  | foptime,fbizappid,fuserid |
| 4 | t_log_app_pkey |  | fid |
