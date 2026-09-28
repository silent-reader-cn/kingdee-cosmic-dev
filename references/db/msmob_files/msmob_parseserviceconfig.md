# 码解析服务配置-msmob_parseserviceconfig

## 码解析服务配置-多语言表 t_msmob_parseservice_l

- **表名称：** 码解析服务配置-多语言表
- **表名：** t_msmob_parseservice_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 码解析服务名称 | varchar | 50 |  | √ | ' ' | 码解析服务名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fexplanation | 码解析服务说明 | varchar | 255 |  |  | null | 码解析服务说明 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msmob_parseservice_l |  | fpkid |
| 2 | idx_msmob_parseservice_l_fid |  | fid |

---

## 码解析服务配置-主表 t_msmob_parseservice

- **表名称：** 码解析服务配置-主表
- **表名：** t_msmob_parseservice

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 码解析服务名称 | varchar | 50 |  | √ | ' ' | 码解析服务名称 |
| 3 | fmethodname | 调用服务方法 | varchar | 50 |  | √ | ' ' | 调用服务方法 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fpriority | 码解析服务优先级 | numeric | 23 | 10 | √ | 0 | 码解析服务优先级 |
| 7 | fispreset | 系统预置 | bpchar | 1 |  | √ | ' ' | 系统预置 |
| 8 | fexplanation | 码解析服务说明 | varchar | 255 |  | √ | ' ' | 码解析服务说明 |
| 9 | fappid | 应用Id | varchar | 50 |  | √ | ' ' | 应用Id |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fcloudid | 云Id | varchar | 50 |  | √ | ' ' | 云Id |
| 15 | fservicename | 注册服务名称 | varchar | 50 |  | √ | ' ' | 注册服务名称 |
| 16 | fcondition | 码解析条件 | varchar | 512 |  | √ | ' ' | 码解析条件 |
| 17 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 码解析服务编码 | varchar | 30 |  | √ | ' ' | 码解析服务编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mob_parseservice_fpriority |  | fpriority |
| 2 | pk_t_msmob_parseservice |  | fid |
