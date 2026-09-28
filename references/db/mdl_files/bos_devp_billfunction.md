# 函数定义-bos_devp_billfunction

## 函数定义-主表 t_dm_billfunction

- **表名称：** 函数定义-主表
- **表名：** t_dm_billfunction

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdefformula | 默认表达式 | varchar | 200 |  | √ | ' ' | 默认表达式 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fclassname | 函数运行类 | varchar | 200 |  | √ | ' ' | 函数运行类 |
| 6 | fisv | 开发商 | varchar | 30 |  | √ | ' ' | 开发商 |
| 7 | fshowseq | 显示顺序 | int4 | 32 |  | √ | 0 | 显示顺序 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | freturntype | 返回值类型 | varchar | 30 |  | √ | 'Object' | 返回值类型,枚举: int :整数 long :长整数 String :字符串 boolean :布尔值 date :日期 BigDecimal :小数 Object :其他 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fissys | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 12 | ffunctype | 函数适用范围 | varchar | 30 |  | √ | 'bill' | 函数适用范围,枚举: bill :单据函数：适用于业务规则、校验器 common :通用函数：适用于所有场景 |
| 13 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 15 | fsysdisable | 已废弃 | bpchar | 1 |  | √ | '0' | 已废弃 |
| 16 | fformid | 参数配置界面 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_dm_billfunction |  | fid |
| 2 | idx_dm_billfunction_num |  | fnumber |

---

## 函数定义-多语言表 t_dm_billfunction_l

- **表名称：** 函数定义-多语言表
- **表名：** t_dm_billfunction_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 4 | fdesc | 函数使用说明 | varchar | 500 |  | √ | ' ' | 函数使用说明 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_dm_billfunction_l |  | fpkid |
| 2 | idx_dm_billfunction_l_id |  | fid |
