# 制造策略-bd_manustrategy

## 制造策略-多语言表 t_bd_manustrategy_l

- **表名称：** 制造策略-多语言表
- **表名：** t_bd_manustrategy_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 策略名称 | varchar | 364 |  | √ | ' ' | 策略名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_manustrategy_l |  | fid,flocaleid |
| 2 | pk_t_bd_manustrategy_l |  | fpkid |

---

## 追溯维度-多选基础资料表 t_bd_manustrategy_way

- **表名称：** 追溯维度-多选基础资料表
- **表名：** t_bd_manustrategy_way

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [制造策略维度 bd_manustrategydim](../sbd_files/bd_manustrategydim.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_manustrategy_way |  | fid |
| 2 | pk_t_bd_manustrategy_way |  | fpkid |

---

## 库存隔离维度-多选基础资料表 t_bd_manustrategy_inv

- **表名称：** 库存隔离维度-多选基础资料表
- **表名：** t_bd_manustrategy_inv

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [制造策略维度 bd_manustrategydim](../sbd_files/bd_manustrategydim.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_manustrategy_inv |  | fid |
| 2 | pk_t_bd_manustrategy_inv |  | fpkid |

---

## 追溯范围-多选基础资料表 t_bd_manustrategy_range

- **表名称：** 追溯范围-多选基础资料表
- **表名：** t_bd_manustrategy_range

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [制造策略领域(供应链) bd_manustrategydomain](../sbd_files/bd_manustrategydomain.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bd_manustrategy_range |  | fpkid |
| 2 | idx_bd_manustrategy_range |  | fid |

---

## 制造策略-主表 t_bd_manustrategy

- **表名称：** 制造策略-主表
- **表名：** t_bd_manustrategy

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 策略名称 | varchar | 364 |  | √ | ' ' | 策略名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fisinway | 考虑在途/在制 | bpchar | 1 |  | √ | '0' | 考虑在途/在制 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fdemandmodel | 计划模式 | varchar | 30 |  | √ | ' ' | 计划模式,枚举: MTS :MTS MTO :MTO ETO :ETO PTO :PTO |
| 7 | fiscurrentstock | 考虑即时库存 | bpchar | 1 |  | √ | '0' | 考虑即时库存 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fchildsetoff | 子项预测冲减 | bpchar | 1 |  | √ | '0' | 子项预测冲减 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fissystem | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 14 | fenable | 使用状态 | varchar | 10 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fnumber | 策略编码 | varchar | 50 |  | √ | ' ' | 策略编码 |
| 16 | fissafestock | 考虑安全库存 | bpchar | 1 |  | √ | '0' | 考虑安全库存 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_manustrategy |  | fnumber |
| 2 | pk_t_bd_manustrategy |  | fid |

---

## 不更新库存维度(后台)-多选基础资料表 t_bd_manustrategy_no_inv

- **表名称：** 不更新库存维度(后台)-多选基础资料表
- **表名：** t_bd_manustrategy_no_inv

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [制造策略维度 bd_manustrategydim](../sbd_files/bd_manustrategydim.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bd_manustrategy_no_inv |  | fpkid |
| 2 | idx_bd_manustrategy_no_inv |  | fid |
