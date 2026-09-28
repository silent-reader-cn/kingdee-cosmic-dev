# 业务节点-pds_biznode

## 业务节点-多语言表 t_pds_biznode_l

- **表名称：** 业务节点-多语言表
- **表名：** t_pds_biznode_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 300 |  | √ | ' ' | 备注 |
| 3 | fname | 节点名称 | varchar | 300 |  | √ | ' ' | 节点名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pds_biznode_l_fid |  | fid,flocaleid |
| 2 | pk_pds_biznode_l |  | fpkid |
| 3 | idx_pds_biznode_l_fname |  | fname |

---

## 业务节点-主表 t_pds_biznode

- **表名称：** 业务节点-主表
- **表名：** t_pds_biznode

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | fremark | varchar | 300 |  | √ | ' ' |  |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fname | 节点名称 | varchar | 300 |  | √ | ' ' | 节点名称 |
| 5 | ftemplateid | 默认的组件模板 | int8 | 64 |  | √ | 0 | 组件模板配置 pds_tplconfig |
| 6 | fissupplier | 供应商端节点 | bpchar | 1 |  | √ | '0' | 供应商端节点 |
| 7 | fbizobject | 节点对应的业务对象 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 8 | fischangenode | 允许发起变更的节点 | bpchar | 1 |  | √ | '0' | 允许发起变更的节点 |
| 9 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fisautonextnode | 审核后自动跳转到下一个节点 | bpchar | 1 |  | √ | '1' | 审核后自动跳转到下一个节点 |
| 12 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fisautoclose | 跳转后自动关闭当前节点 | bpchar | 1 |  | √ | '1' | 跳转后自动关闭当前节点 |
| 16 | fuserplugin | 获取节点用户插件 | varchar | 100 |  | √ | ' ' | 获取节点用户插件 |
| 17 | fextobject | 节点对应的状态表 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 18 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fnumber | 节点编码 | varchar | 30 |  | √ | ' ' | 节点编码 |
| 20 | fissyspreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 21 | fpluginname | 获取节点状态插件 | varchar | 100 |  | √ | ' ' | 获取节点状态插件 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pds_biznode_fbizobject |  | fbizobject |
| 2 | idx_pds_biznode_fextobject |  | fextobject |
| 3 | idx_pds_biznode_fmasterid |  | fmasterid |
| 4 | idx_pds_biznode_fcreatetime |  | fcreatetime |
| 5 | idx_pds_biznode_fnumber |  | fnumber |
| 6 | pk_pds_biznode |  | fid |
