# 服务租户-aicc_tenant

## 服务租户-主表 t_aicc_tenant

- **表名称：** 服务租户-主表
- **表名：** t_aicc_tenant

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 租户名称 | varchar | 200 |  | √ | ' ' | 租户名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcqtenantid | 苍穹租户ID | varchar | 200 |  | √ | ' ' | 苍穹租户ID |
| 5 | fprodinstid | 苍穹产品实例码 | varchar | 200 |  | √ | ' ' | 苍穹产品实例码 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fbuyqps | 购买的QPS | int8 | 64 |  | √ | 0 | 购买的QPS |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | ftenanttype | 租户类型 | varchar | 50 |  | √ | ' ' | 租户类型,枚举: public :公有云 private :私有云 mix :混合云 |
| 13 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :暂停服务 1 :服务中 |
| 14 | fnumber | 租户编码 | varchar | 30 |  | √ | ' ' | 租户编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_aicc_tenant |  | fid |
| 2 | idx_aicc_tenant_fnumber |  | fnumber |

---

## 服务租户-多语言表 t_aicc_tenant_l

- **表名称：** 服务租户-多语言表
- **表名：** t_aicc_tenant_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 租户名称 | varchar | 50 |  | √ | ' ' | 租户名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_aicc_tenant_l_fid |  | fid |
| 2 | pk_t_aicc_tenant_l |  | fpkid |
