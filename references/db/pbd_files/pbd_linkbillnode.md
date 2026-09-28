# 单据联查节点-pbd_linkbillnode

## 单据联查节点-主表 t_pbd_linkbillnode

- **表名称：** 单据联查节点-主表
- **表名：** t_pbd_linkbillnode

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | fname | 执行配置 | varchar | 2000 |  | √ | ' ' | 执行配置 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fnodedesc | 节点执行描述 | varchar | 512 |  | √ | ' ' | 节点执行描述 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fbizappid | 所属应用 | varchar | 36 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fdefinelinkid | 联查配置 | varchar | 36 |  | √ | ' ' | 联查关系定义 pbd_definelinkbill |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | ftargetentityid | 目标实体 | varchar | 36 |  | √ | ' ' | 单据主实体 bos_billmainentity |
| 11 | fpreset | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |
| 12 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 13 | fsourceentityid | 主单据实体 | varchar | 36 |  | √ | ' ' | 单据主实体 bos_billmainentity |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pbd_linkbillnode |  | fid |
| 2 | idx_pbd_linkbillnode_fnumber |  | fnumber |
