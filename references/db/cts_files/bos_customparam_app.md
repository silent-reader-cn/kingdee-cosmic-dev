# 应用参数_自定义参数-bos_customparam_app

## 应用参数_自定义参数-多语言表 t_svc_customparam_app_l

- **表名称：** 应用参数_自定义参数-多语言表
- **表名：** t_svc_customparam_app_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 参数说明 | varchar | 797 |  | √ | ' ' | 参数说明 |
| 3 | flocaleid | flocaleid | varchar | 20 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_customparam_app_l_n |  | fid,flocaleid |
| 2 | pk_t_svc_customparam_app_l |  | fpkid |

---

## 应用参数_自定义参数-主表 t_svc_customparam_app

- **表名称：** 应用参数_自定义参数-主表
- **表名：** t_svc_customparam_app

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 参数说明 | varchar | 797 |  | √ | ' ' | 参数说明 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fappid | 应用id | varchar | 36 |  | √ | ' ' | 应用id |
| 7 | fvalue | 参数值 | varchar | 255 |  | √ | ' ' | 参数值 |
| 8 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | varchar | 50 |  | √ | ' ' | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmasterid | 主数据内码 | varchar | 36 |  | √ | ' ' | 主数据内码 |
| 11 | fkey | 参数名称 | varchar | 80 |  | √ | ' ' | 参数名称 |
| 12 | fsort | 排序 | int4 | 32 |  | √ | 0 | 排序 |
| 13 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_customparam_app_n |  | fnumber |
| 2 | pk_t_svc_customparam_app |  | fid |
