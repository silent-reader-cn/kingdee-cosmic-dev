# 上机操作日志-bos_log_operation_web

## 上机操作日志-多语言表 t_log_app_v2_l

- **表名称：** 上机操作日志-多语言表
- **表名：** t_log_app_v2_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' |  |
| 2 | fopname | 操作名称 | varchar | 255 |  | √ | ' ' | 操作名称 |
| 3 | fopdescription | 操作描述 | varchar | 255 |  | √ | ' ' | 操作描述 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fclientname | 客户端名称 | varchar | 255 |  | √ | ' ' | 客户端名称 |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid,fid |
| 2 | fid | fpkid,fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_log_app_v2_l_0 |  | fid,flocaleid |
| 2 | pk_log_app_v2_l |  | fpkid,fid |

---

## 上机操作日志-主表 t_log_app_v2

- **表名称：** 上机操作日志-主表
- **表名：** t_log_app_v2

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | fbizobjname | 操作对象名 | varchar | 255 |  | √ | ' ' | 操作对象名 |
| 3 | fmodifybillid | 数据更新源单内码 | varchar | 36 |  | √ | ' ' | 数据更新源单内码 |
| 4 | forgid | 操作组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fclienttype | 客户端类型 | varchar | 30 |  | √ | ' ' | 客户端类型,枚举: web :PC端 mobile :移动端 |
| 6 | fbizappname | 应用名 | varchar | 255 |  | √ | ' ' | 应用名 |
| 7 | fuserid | 操作用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fmodifybillno | 数据更新源单编码 | varchar | 255 |  | √ | ' ' | 数据更新源单编码 |
| 9 | fmodifycontent_tag | 数据更新内容_详情 | text | 0 |  |  | null | 数据更新内容_详情 |
| 10 | fmodifyfields | 数据更新字段 | varchar | 1020 |  | √ | ' ' | 数据更新字段 |
| 11 | farchivetime | 归档时间 | timestamp | 0 |  |  | null | 归档时间 |
| 12 | fbizappid | 应用 | varchar | 36 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |
| 13 | fusername | 操作用户名 | varchar | 255 |  | √ | ' ' | 操作用户名 |
| 14 | fclientip | 客户端地址 | varchar | 128 |  | √ | ' ' | 客户端地址 |
| 15 | fclientnamee | 客户端名称名 | varchar | 255 |  | √ | ' ' | 客户端名称名 |
| 16 | foptime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 17 | fopdescriptione | 操作描述名 | varchar | 255 |  | √ | ' ' | 操作描述名 |
| 18 | fmodifycontent | 数据更新内容 | varchar | 510 |  |  | null | 数据更新内容 |
| 19 | fopnamee | 操作名称名 | varchar | 255 |  | √ | ' ' | 操作名称名 |
| 20 | fbizobjid | 操作对象 | varchar | 36 |  | √ | ' ' | 业务对象 bos_objecttype |
| 21 | forgname | 操作组织名 | varchar | 255 |  | √ | ' ' | 操作组织名 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_log_appv2_modifybillid |  | fmodifybillid |
| 2 | pk_t_log_app_v2 |  | fid |
| 3 | idx_log_appv2_optimeappuser |  | foptime,fbizappid,fuserid |
