# 校验器-bos_devp_validation

## 应用范围-多选基础资料表 t_dm_validatorapprange

- **表名称：** 应用范围-多选基础资料表
- **表名：** t_dm_validatorapprange

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
| 1 | pk_dm_validatorapprange |  | fpkid |
| 2 | idx_dm_validatorapprange_fk |  | fid |

---

## 校验器-多语言表 t_dm_validator_l

- **表名称：** 校验器-多语言表
- **表名：** t_dm_validator_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdesc | 描述 | varchar | 500 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_dm_validator_l_fk |  | fid |
| 2 | pk_dm_validator_l |  | fpkid |

---

## 校验器-主表 t_dm_validator

- **表名称：** 校验器-主表
- **表名：** t_dm_validator

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fopblacklist | 操作类型黑名单 | varchar | 1000 |  |  | null | 操作类型黑名单,枚举: |
| 3 | ferrorlevel | 错误级别 | varchar | 50 |  |  | null | 错误级别,枚举: 0 :红色错误，立即终止 1 :警告，允许忽略 2 :黄色警告，立即终止 3 :绿色提示 |
| 4 | frange | 适用范围 | varchar | 10 |  | √ | ' ' | 适用范围,枚举: all :全部 app :应用 |
| 5 | fisv | 开发商标识 | varchar | 10 |  | √ | ' ' | 开发商标识 |
| 6 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 7 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 8 | frunclass | 实现类 | varchar | 500 |  |  | null | 实现类 |
| 9 | fformid | 定义参数 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 10 | fopwhitelist | 操作类型白名单 | varchar | 1000 |  |  | null | 操作类型白名单,枚举: |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_dm_validator |  | fid |
| 2 | idx_t_dm_validator_number |  | fnumber |
