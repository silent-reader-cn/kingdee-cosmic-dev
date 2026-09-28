# 服务目录-evt_service

## 服务目录-多语言表 t_evt_service_l

- **表名称：** 服务目录-多语言表
- **表名：** t_evt_service_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 服务名称 | varchar | 300 |  | √ | ' ' | 服务名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_evt_service_l_pkey |  | fpkid |
| 2 | idx_evt_service_l |  | fid,flocaleid |

---

## 服务目录-主表 t_evt_service

- **表名称：** 服务目录-主表
- **表名：** t_evt_service

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 服务名称 | varchar | 100 |  | √ | ' ' | 服务名称 |
| 3 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | finnerservice | 内置服务 | bpchar | 1 |  | √ | '0' | 内置服务 |
| 5 | fstatus | 服务启用 | bpchar | 1 |  | √ | '1' | 服务启用,枚举: 0 :禁用 1 :启用 |
| 6 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | ftype | 实现类型 | varchar | 30 |  | √ | ' ' | 实现类型,枚举: java :java服务 script :脚本服务 http :HTTP服务 |
| 8 | fconfig | 服务配置页面 | varchar | 36 |  | √ | ' ' | 表单元数据 bos_formmeta |
| 9 | fapp | 所属应用 | varchar | 36 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |
| 10 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fscene | 服务应用场景 | varchar | 100 |  | √ | ' ' | 服务应用场景 |
| 13 | fimplementation | 服务实现 | varchar | 400 |  | √ | ' ' | 服务实现 |
| 14 | fnumber | 服务编码 | varchar | 500 |  | √ | ' ' | 服务编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_evt_service_pkey |  | fid |
| 2 | idx_evt_service_number |  | fnumber |
