# 库存单据字段锁定设置-im_billfieldenablesetting

## 字段分录-子表 t_im_fieldenablesetentry

- **表名称：** 字段分录-子表
- **表名：** t_im_fieldenablesetentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fisauditdisable | 审核锁定 | bpchar | 1 |  | √ | '0' | 审核锁定 |
| 3 | ffieldname | 字段名称 | varchar | 50 |  | √ | ' ' | 字段名称 |
| 4 | ffield | 字段标识 | varchar | 50 |  | √ | ' ' | 字段标识 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fentryentityid | 单据体标识 | varchar | 50 |  | √ | ' ' | 单据体标识 |
| 8 | ffullfield | 字段全标识 | varchar | 50 |  | √ | ' ' | 字段全标识 |
| 9 | fisdrawdisable | 关联锁定 | bpchar | 1 |  | √ | '0' | 关联锁定 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_im_fieldenablesetentry |  | fentryid |
| 2 | idx_im_fieldenablesetentry_fk |  | fid |

---

## 库存单据字段锁定设置-主表 t_im_fieldenableset

- **表名称：** 库存单据字段锁定设置-主表
- **表名：** t_im_fieldenableset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmininvqty | fmininvqty | numeric | 23 | 10 | √ | 0 |  |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fbill | 单据 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 8 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 9 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_im_fieldenableset |  | fid |

---

## 库存单据字段锁定设置-多语言表 t_im_fieldenableset_l

- **表名称：** 库存单据字段锁定设置-多语言表
- **表名：** t_im_fieldenableset_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_im_fieldenableset_l |  | fpkid |
| 2 | idx_im_fieldenableset_l_0 |  | fid,flocaleid |
