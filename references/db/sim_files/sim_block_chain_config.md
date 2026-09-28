# 区块链第三方配置-sim_block_chain_config

## 区块链第三方配置-主表 t_sim_block_chain_config

- **表名称：** 区块链第三方配置-主表
- **表名：** t_sim_block_chain_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fepid | 企业组织id | varchar | 50 |  | √ | ' ' | 企业组织id |
| 3 | feccprikey | ecc私钥 | varchar | 256 |  | √ | ' ' | ecc私钥 |
| 4 | frsapubkey | rsa公钥 | varchar | 1024 |  | √ | ' ' | rsa公钥 |
| 5 | fsmprikey | sm私钥 | varchar | 128 |  | √ | ' ' | sm私钥 |
| 6 | faddress | 企业地址 | varchar | 256 |  | √ | ' ' | 企业地址 |
| 7 | fsmpubkey | sm公钥 | varchar | 256 |  | √ | ' ' | sm公钥 |
| 8 | ftype | 企业开票类型 | varchar | 50 |  | √ | ' ' | 企业开票类型 |
| 9 | frsaprikey | rsa私钥 | varchar | 1024 |  | √ | ' ' | rsa私钥 |
| 10 | fspvpubkeybase64 | spv公钥base64 | varchar | 512 |  | √ | ' ' | spv公钥base64 |
| 11 | feccpubkey | ecc公钥 | varchar | 128 |  | √ | ' ' | ecc公钥 |
| 12 | fcompanyid | 企业id | varchar | 50 |  | √ | ' ' | 企业id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sim_block_chain_config |  | fid |
| 2 | idx_sim_block_chain_config |  | fepid |
