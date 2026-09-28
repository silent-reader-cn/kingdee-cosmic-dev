# 检修工单编码规则配置-pom_mrotranstype_coderule

## 检修工单编码规则配置-主表 t_pom_transtypecoderule

- **表名称：** 检修工单编码规则配置-主表
- **表名：** t_pom_transtypecoderule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fmrotranstypeid | 检修事务类型 | int8 | 64 |  | √ | 0 | 生产事务类型 mpdm_transactproduct |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fisinterruptno | 断号回收 | bpchar | 1 |  | √ | '0' | 断号回收 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 12 | fcontcharrangle | 常量字符范围 | varchar | 80 |  | √ | ' ' | 常量字符范围 |
| 13 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 14 | fcodetype | 编码生成方式 | varchar | 50 |  | √ | ' ' | 编码生成方式,枚举: A :项目号+常量+流水号+校验码 B :源单单据编号+常量+流水号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pom_transtypecoderule |  | fid |
| 2 | idx_pom_typerule_typeid |  | fmrotranstypeid |

---

## 检修工单编码规则配置-多语言表 t_pom_transtypecoderule_l

- **表名称：** 检修工单编码规则配置-多语言表
- **表名：** t_pom_transtypecoderule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pom_transtypecoderule_l |  | fpkid |
| 2 | idx_pom_transtcodel_l |  | fid,flocaleid |
