# 供应商准入节点-srm_accessnode

## 供应商准入节点-主表 t_srm_accessnode

- **表名称：** 供应商准入节点-主表
- **表名：** t_srm_accessnode

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 3 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 4 | fstatus | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 5 | fmandatory | 必选节点 | bpchar | 1 |  | √ | '0' | 必选节点 |
| 6 | fbizobject | 业务单据 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 7 | fpreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 8 | fserviceclass | 服务处理类 | varchar | 255 |  | √ | ' ' | 服务处理类 |
| 9 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_srm_accessnode |  | fid |
| 2 | idx_accessnode_bizobject |  | fbizobject |
| 3 | idx_accessnode_number |  | fnumber |

---

## 供应商准入节点-多语言表 t_srm_accessnode_l

- **表名称：** 供应商准入节点-多语言表
- **表名：** t_srm_accessnode_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 3 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_srm_accessnode_l |  | fpkid |
| 2 | idx_accessnode_local |  | fid,flocaleid |
