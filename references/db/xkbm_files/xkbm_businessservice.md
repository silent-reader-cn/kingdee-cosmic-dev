# 预算业务服务-xkbm_businessservice

## 预算业务服务-主表 t_xkbm_businessservice

- **表名称：** 预算业务服务-主表
- **表名：** t_xkbm_businessservice

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 模块名称 | varchar | 255 |  | √ | ' ' | 模块名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcoderulehead | 编码规则前缀 | varchar | 50 |  | √ | ' ' | 编码规则前缀 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fappname | 服务业务模块 | varchar | 30 |  | √ | ' ' | 服务业务模块,枚举: 0 :费用管理 1 :项目管理 2 :总账 3 :经营会计 99 :不限 |
| 12 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 13 | fnumber | 模块编码 | varchar | 50 |  | √ | ' ' | 模块编码 |
| 14 | fissyspreset | 系统预置 | bpchar | 1 |  | √ | ' ' | 系统预置 |
| 15 | fforbiddate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 16 | fforbidderid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_businessservice |  | fnumber |
| 2 | pk_xkbm_businessservice |  | fid |

---

## 预算业务类型范围-多选基础资料表 t_xkbm_bizservicetype

- **表名称：** 预算业务类型范围-多选基础资料表
- **表名：** t_xkbm_bizservicetype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 预算业务类型 xkbm_businesstype |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_bizservicetype |  | fpkid |
| 2 | idx_xkbm_bizservicetype |  | fid |

---

## 预算业务服务-多语言表 t_xkbm_businessservice_l

- **表名称：** 预算业务服务-多语言表
- **表名：** t_xkbm_businessservice_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 模块名称 | varchar | 255 |  | √ | ' ' | 模块名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_businessservice_l |  | fpkid |
| 2 | idx_xkbm_businessservice_l |  | fid,flocaleid |
