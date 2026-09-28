# 操作服务-bos_devp_opservice

## 操作服务-多语言表 t_dm_opservice_l

- **表名称：** 操作服务-多语言表
- **表名：** t_dm_opservice_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdesc | 描述 | varchar | 200 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_dm_opservice_l |  | fpkid |
| 2 | idx_t_dm_opservice_l_fk |  | fid |

---

## 所属应用-多选基础资料表 t_dm_opserviceapp

- **表名称：** 所属应用-多选基础资料表
- **表名：** t_dm_opserviceapp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | varchar | 18 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_dm_opserviceapp |  | fpkid |
| 2 | idx_dm_opserviceapp_fk |  | fid |

---

## 操作服务-主表 t_dm_opservice

- **表名称：** 操作服务-主表
- **表名：** t_dm_opservice

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fclass | 实现类 | varchar | 500 |  |  | null | 实现类 |
| 3 | fopblacklist | 操作类型黑名单 | varchar | 1000 |  |  | null | 操作类型黑名单,枚举: |
| 4 | fisdesign | 设计器可见 | bpchar | 1 |  | √ | '1' | 设计器可见 |
| 5 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 6 | fisv | 开发商标识 | varchar | 10 |  | √ | ' ' | 开发商标识 |
| 7 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 8 | fformid | 定义参数 | varchar | 36 |  |  | null | 主实体对象 bos_entityobject |
| 9 | fapplicationrange | 适用范围 | bpchar | 1 |  | √ | '0' | 适用范围,枚举: 0 :全部 1 :应用 |
| 10 | fopwhitelist | 操作类型白名单 | varchar | 1000 |  |  | null | 操作类型白名单,枚举: |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_dm_opservice |  | fid |
| 2 | idx_t_dm_opservice_number |  | fnumber |
